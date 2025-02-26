import os
import sys
import subprocess
import time
from pathlib import Path
import tempfile
import json
import re

# Set CUDA architecture
os.environ["TORCH_CUDA_ARCH_LIST"] = "8.9"

# Find CUDA in conda environment
conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    cuda_path = Path(conda_prefix) / 'lib' / 'cuda'
    if not cuda_path.exists():
        cuda_path = Path(conda_prefix)
    os.environ['CUDA_HOME'] = str(cuda_path)

# Enable compilation database generation
os.environ["TORCH_COMPILE_DB"] = "1"

import torch
from torch.utils.cpp_extension import load_inline

# Test different header combinations
header_combinations = [
    # Default (implicit torch/torch.h through PyTorch)
    {
        "name": "implicit_default",
        "cpp": """
torch::Tensor to_gray(torch::Tensor input);
""",
        "cuda": """
torch::Tensor to_gray(torch::Tensor input) {
  auto output = torch::empty({input.size(0), input.size(1)}, input.options());  
  return output; 
}
"""
    },
    
    # Explicit torch/torch.h
    {
        "name": "explicit_torch_h",
        "cpp": """
#include <torch/torch.h>
torch::Tensor to_gray(torch::Tensor input);
""",
        "cuda": """
#include <torch/torch.h>
torch::Tensor to_gray(torch::Tensor input) {
  auto output = torch::empty({input.size(0), input.size(1)}, input.options());  
  return output; 
}
"""
    },
    
    # Minimal includes
    {
        "name": "minimal_includes",
        "cpp": """
#include <c10/core/TensorOptions.h>
#include <torch/types.h>
torch::Tensor to_gray(torch::Tensor input);
""",
        "cuda": """
#include <c10/core/TensorOptions.h>
#include <ATen/core/TensorBody.h>
#include <c10/util/ArrayRef.h>
torch::Tensor to_gray(torch::Tensor input) {
  auto output = torch::empty({input.size(0), input.size(1)}, input.options());  
  return output; 
}
"""
    }
]

def parse_ftime_report(log_text):
    """Parse the -ftime-report output to extract timing data"""
    results = {}
    
    pattern = r'(\s*)([^:]+)(\s*):(\s*)(\d+\.\d+)(\s*)\((\s*)(\d+)(%)\)'
    
    matches = re.findall(pattern, log_text)
    for match in matches:
        phase_name = match[1].strip()
        time_seconds = float(match[4])
        percentage = int(match[7])
        
        results[phase_name] = {
            "time_seconds": time_seconds,
            "percentage": percentage
        }
    
    return results

def test_header_combination(combo, build_root):
    """Test a specific header combination and measure compile time"""
    name = combo["name"]
    cpp_code = combo["cpp"]
    cuda_kernel_code = combo["cuda"]
    
    print(f"\n\n===== Testing {name} =====")
    
    # Create a dedicated build directory for this test
    build_dir = build_root / name
    build_dir.mkdir(exist_ok=True)
    
    # Capture stdout/stderr to get compilation logs
    log_file = build_dir / "compile_log.txt"
    
    # Measure compilation time
    start_time = time.time()
    
    try:
        # Redirect output to capture logs
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        with open(log_file, 'w') as f:
            sys.stdout = f
            sys.stderr = f
            
            # Compile the extension
            cuda_module = load_inline(
                name=f"to_gray_cuda_{name}",
                cpp_sources=cpp_code, 
                cuda_sources=cuda_kernel_code, 
                functions=["to_gray"],
                with_cuda=True,
                verbose=True,
                extra_cflags=["-std=c++17", "-ftime-report"],
                extra_cuda_cflags=["-arch=sm_89"],
                build_directory=str(build_dir),
            )
    except Exception as e:
        print(f"Compilation failed: {e}")
    finally:
        # Restore stdout/stderr
        sys.stdout = original_stdout
        sys.stderr = original_stderr
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Read log file to extract -ftime-report information
    log_content = ""
    try:
        with open(log_file, 'r') as f:
            log_content = f.read()
    except:
        pass
    
    # Parse ftime report data
    ftime_data = parse_ftime_report(log_content)
    
    # Count the number of headers included
    header_count = log_content.count("including")
    
    # Extract template instantiation time if available
    template_time = ftime_data.get("template instantiation", {}).get("time_seconds", 0)
    template_pct = ftime_data.get("template instantiation", {}).get("percentage", 0)
    
    # Print results
    print(f"Compilation time: {total_time:.2f} seconds")
    print(f"Header count (approx): {header_count}")
    print(f"Template instantiation time: {template_time:.2f}s ({template_pct}%)")
    
    # Return metrics
    return {
        "name": name,
        "total_time": total_time,
        "header_count": header_count,
        "template_time": template_time,
        "template_percentage": template_pct,
        "ftime_data": ftime_data
    }

# Create a master build directory
master_build_dir = Path("./pytorch_header_profile")
master_build_dir.mkdir(exist_ok=True)

# Test all combinations
results = []
for combo in header_combinations:
    result = test_header_combination(combo, master_build_dir)
    results.append(result)

# Print comparative results
print("\n\n===== COMPARATIVE RESULTS =====")
print(f"{'Header Combination':<20} | {'Total Time (s)':<15} | {'Header Count':<15} | {'Template Time (s)':<15} | {'Template %':<10}")
print("-" * 80)

for result in results:
    print(f"{result['name']:<20} | {result['total_time']:<15.2f} | {result['header_count']:<15} | {result['template_time']:<15.2f} | {result['template_percentage']:<10}")

# Extract specific header inclusion patterns
def analyze_header_patterns(build_root):
    print("\n\n===== HEADER ANALYSIS =====")
    
    # Common PyTorch headers that might be problematic
    problematic_headers = [
        "ATen/core/TensorBody.h",
        "c10/core/TensorOptions.h",
        "torch/csrc/api/include/torch/nn/modules",
        "torch/csrc/api/include/torch/optim",
        "torch/csrc/jit",
        "torch/csrc/autograd"
    ]
    
    # Check for these headers in the log files
    for name in [combo["name"] for combo in header_combinations]:
        log_file = build_root / name / "compile_log.txt"
        if not log_file.exists():
            continue
            
        print(f"\nAnalyzing {name}:")
        
        with open(log_file, 'r') as f:
            log_content = f.read()
            
        for header in problematic_headers:
            count = log_content.count(header)
            if count > 0:
                print(f"  - {header}: included {count} times")

analyze_header_patterns(master_build_dir)

print("\n\nConclusion: The results above show which header combinations lead to faster compilation times.")
print("For production code, consider using the minimal includes approach and creating a precompiled header.")