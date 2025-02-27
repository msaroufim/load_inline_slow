## Analysis
1. `benchmark_load_inline.py` is the basic benchmark script. Most of the user time is in template instantiation and parsing - about 40s if we include torch headers but drops to 1s with just cuda headers (inspect the built logs https://github.com/msaroufim/load_inline_slow/tree/main/torch_extension_build, remove pytorch headers and run the ninja build scripts directly)
2. header-analysis shows all the headers that get pulled in - about 90% of the files are torch specific and not python or linux. There's about 4700/5200 files that get pulled in all torch specific. torch_types pulls in about 17K files
3. iwyu analysis shows that minimal inclues can be faster than default includes (this didn't work too well but is on the right track to figure out what are the right minimal set of dependencies)
4. cprofile-analysis shows output of profile with cprofile - a lot of file reading and path resolution and initializing pytorch 529 lines with general file-related keywords, 176 Python file operation references, 232 importlib references
5. line profiler not helpful

## Description of the problem

We want a way to mix in cuda code in a pytorch program in a way that takes less than 5s. Right now the leaderboard takes 5s to provision a machine and run a triton kernel wheras building a toy cuda kernel takes 40-60s.

Solution space is
1. Make people build a python package for a specific cuda version elsewhere and then pull it
2. We build those python packages for people
3. We make load inline only get what it needs and do whatever refactoring we need in aten
4. We make a load inline fast that just c pointer a la deepseek or bnb 

## Plan for what to do next
1. Build a no-headers mode for load_inline
2. Build tribal knowledge around which headers are mostly needed for the leaderboard (most likely we just need to keep exception.h, basetensor which a tensor without methods
3. Do the complete exit hatch a la deepseek or bnb with c pointers if 2 is not possible https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/jit/template.py
4. Think harder about how to restructure aten with minimal baseline dependencies (needs work)

## Things to look into next
1. Are we doing something dumb in python or c++?
2. Including `TensorBase.h` and that will pull in close to nothing https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/core/TensorBase.h and we can just share an example assuming people aren't using aten ops
3. If you want torch.empty you want empty.h (these headers were built by design to be slim)
4. Deranged file https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cpp_custom_type_hack.h


## Profiling tools that might be helpful

1. export NINJA_STATUS="[%f/%t %o/s %es] "
2. extra_cflags=["-ftime-trace", "-std=c++17"]
3. pip install iwyu
4. os.environ["TORCH_COMPILE_DB"] = "1"
5. import cProfile; cProfile.run('import your_module', 'profile_output')
6. pip install line_profiler
7. extra_cflags=["-H", "-std=c++17", "-ftime-report"]
8. extra_cflags=["-std=c++17", "-ftemplate-backtrace-limit=0"]
9. extra_cflags=["-ftime-trace", "-std=c++17"]
