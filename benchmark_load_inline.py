import os
os.environ["TORCH_CUDA_ARCH_LIST"] = "8.9"
import sys
from pathlib import Path
import shutil
import tempfile

# Find CUDA in conda environment
conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    cuda_path = Path(conda_prefix) / 'lib' / 'cuda'
    if not cuda_path.exists():
        cuda_path = Path(conda_prefix)
    os.environ['CUDA_HOME'] = str(cuda_path)

import torch
from torch.utils.cpp_extension import load_inline

cpp_code = """
torch::Tensor to_gray(torch::Tensor input);
"""

cuda_kernel_code = """
torch::Tensor to_gray(torch::Tensor input) {
  auto output = torch::empty({input.size(0), input.size(1)}, input.options());  
  return output ; 
}
"""

# Avoid caching results
with tempfile.TemporaryDirectory() as build_dir:
    cuda_module = load_inline(
        name="to_gray_cuda",
        cpp_sources=cpp_code, 
        cuda_sources=cuda_kernel_code, 
        functions=["to_gray"],
        with_cuda=True,
        verbose=True,
        extra_cflags=["-std=c++17", "-ftime-report"],
        extra_cuda_cflags=["-arch=sm_89"],
        build_directory=build_dir,
    )