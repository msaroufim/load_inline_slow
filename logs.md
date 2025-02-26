## extra_cflags=["-std=c++17", "-ftime-report"],


```

(pt) mark@mark:~/Dev/test$ python benchmark_load_inline.py 
Detected CUDA files, patching ldflags
Emitting ninja build file /tmp/tmp8tqb7z3c/build.ninja...
Building extension module to_gray_cuda...
Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N)
[1/3] /home/mark/anaconda3/envs/pt/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_89,code=sm_89 --compiler-options '-fPIC' -arch=sm_89 -std=c++17 -c /tmp/tmp8tqb7z3c/cuda.cu -o cuda.cuda.o 
[2/3] c++ -MMD -MF main.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -std=c++17 -std=c++17 -ftime-report -c /tmp/tmp8tqb7z3c/main.cpp -o main.o 

Time variable                                   usr           sys          wall           GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)  1423k (  0%)
 phase parsing                      :   6.86 ( 60%)   6.93 ( 75%)  13.78 ( 67%)  1266M ( 68%)
 phase lang. deferred               :   2.66 ( 23%)   1.86 ( 20%)   4.52 ( 22%)   457M ( 25%)
 phase opt and generate             :   1.93 ( 17%)   0.47 (  5%)   2.41 ( 12%)   127M (  7%)
 |name lookup                       :   1.67 ( 15%)   1.38 ( 15%)   3.21 ( 15%)    43M (  2%)
 |overload resolution               :   2.93 ( 26%)   2.34 ( 25%)   5.08 ( 25%)   485M ( 26%)
 garbage collection                 :   1.59 ( 14%)   0.00 (  0%)   1.56 (  8%)     0  (  0%)
 dump files                         :   0.06 (  1%)   0.08 (  1%)   0.22 (  1%)     0  (  0%)
 callgraph construction             :   0.21 (  2%)   0.02 (  0%)   0.25 (  1%)    14M (  1%)
 callgraph optimization             :   0.03 (  0%)   0.03 (  0%)   0.04 (  0%)     0  (  0%)
 callgraph ipa passes               :   0.08 (  1%)   0.08 (  1%)   0.16 (  1%)  7973k (  0%)
 ipa function summary               :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)  2512  (  0%)
 ipa inheritance graph              :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)   102k (  0%)
 ipa free lang data                 :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 ipa free inline summary            :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 cfg construction                   :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)   560k (  0%)
 cfg cleanup                        :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)    12k (  0%)
 trivially dead code                :   0.00 (  0%)   0.03 (  0%)   0.00 (  0%)     0  (  0%)
 df scan insns                      :   0.04 (  0%)   0.03 (  0%)   0.04 (  0%)   111k (  0%)
 df live regs                       :   0.01 (  0%)   0.00 (  0%)   0.04 (  0%)     0  (  0%)
 df reg dead/unused notes           :   0.00 (  0%)   0.00 (  0%)   0.05 (  0%)   947k (  0%)
 register information               :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 preprocessing                      :   0.61 (  5%)   1.23 ( 13%)   1.97 ( 10%)    89M (  5%)
 parser (global)                    :   0.92 (  8%)   1.49 ( 16%)   2.28 ( 11%)   267M ( 14%)
 parser struct body                 :   0.62 (  5%)   0.62 (  7%)   1.16 (  6%)   110M (  6%)
 parser enumerator list             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)   912k (  0%)
 parser function body               :   0.16 (  1%)   0.06 (  1%)   0.30 (  1%)  9592k (  1%)
 parser inl. func. body             :   0.64 (  6%)   0.38 (  4%)   0.98 (  5%)    79M (  4%)
 parser inl. meth. body             :   0.58 (  5%)   0.40 (  4%)   1.04 (  5%)    93M (  5%)
 template instantiation             :   4.93 ( 43%)   4.29 ( 46%)   9.27 ( 45%)  1059M ( 57%)
 constant expression evaluation     :   0.24 (  2%)   0.25 (  3%)   0.49 (  2%)    12M (  1%)
 inline parameters                  :   0.00 (  0%)   0.01 (  0%)   0.02 (  0%)   473k (  0%)
 integration                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)    94k (  0%)
 tree gimplify                      :   0.01 (  0%)   0.03 (  0%)   0.00 (  0%)  8527k (  0%)
 tree eh                            :   0.01 (  0%)   0.01 (  0%)   0.00 (  0%)  1813k (  0%)
 tree CFG construction              :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)  3813k (  0%)
 tree CFG cleanup                   :   0.02 (  0%)   0.01 (  0%)   0.01 (  0%)  4400  (  0%)
 tree SSA rewrite                   :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)  1520k (  0%)
 tree SSA other                     :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)   338k (  0%)
 tree operand scan                  :   0.03 (  0%)   0.01 (  0%)   0.01 (  0%)  3409k (  0%)
 tree switch lowering               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)    19k (  0%)
 dominance computation              :   0.01 (  0%)   0.01 (  0%)   0.02 (  0%)     0  (  0%)
 out of ssa                         :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)   249k (  0%)
 expand vars                        :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)   865k (  0%)
 expand                             :   0.06 (  1%)   0.02 (  0%)   0.05 (  0%)    12M (  1%)
 post expand cleanups               :   0.02 (  0%)   0.02 (  0%)   0.03 (  0%)  2065k (  0%)
 varconst                           :   0.08 (  1%)   0.07 (  1%)   0.03 (  0%)   348k (  0%)
 jump                               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 loop init                          :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)  1869k (  0%)
 loop fini                          :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 integrated RA                      :   0.15 (  1%)   0.05 (  1%)   0.15 (  1%)    57M (  3%)
 LRA non-specific                   :   0.07 (  1%)   0.04 (  0%)   0.09 (  0%)   393k (  0%)
 LRA virtuals elimination           :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)   985k (  0%)
 LRA create live ranges             :   0.01 (  0%)   0.01 (  0%)   0.00 (  0%)    23k (  0%)
 LRA hard reg assignment            :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 reload                             :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)    55k (  0%)
 thread pro- & epilogue             :   0.02 (  0%)   0.00 (  0%)   0.01 (  0%)  3906k (  0%)
 shorten branches                   :   0.04 (  0%)   0.01 (  0%)   0.02 (  0%)     0  (  0%)
 final                              :   0.08 (  1%)   0.00 (  0%)   0.04 (  0%)  4871k (  0%)
 symout                             :   0.00 (  0%)   0.00 (  0%)   0.05 (  0%)     0  (  0%)
 rest of compilation                :   0.12 (  1%)   0.04 (  0%)   0.24 (  1%)  6081k (  0%)
 repair loop structures             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 TOTAL                              :  11.45          9.26         20.72         1852M
[3/3] c++ main.o cuda.cuda.o -shared -L/home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/lib -lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda -ltorch -ltorch_python -L/home/mark/anaconda3/envs/pt/lib -lcudart -o to_gray_cuda.so
Loading extension module to_gray_cuda...
(pt) mark@mark:~/Dev/test$ ^C
(pt) mark@mark:~/Dev/test$ 
```

## IWYU analysis 

sudo apt-get install iwyu


```
(pt) mark@mark:~/Dev/test$ ^C
(pt) mark@mark:~/Dev/test$ python iwyu_analysis.py 


===== Testing implicit_default =====
[1/3] /home/mark/anaconda3/envs/pt/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_implicit_default -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_89,code=sm_89 --compiler-options '-fPIC' -arch=sm_89 -std=c++17 -c /mnt/data/Dev/test/pytorch_header_profile/implicit_default/cuda.cu -o cuda.cuda.o 
[2/3] c++ -MMD -MF main.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_implicit_default -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -std=c++17 -std=c++17 -ftime-report -c /mnt/data/Dev/test/pytorch_header_profile/implicit_default/main.cpp -o main.o 

Time variable                                   usr           sys          wall           GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)  1423k (  0%)
 phase parsing                      :   7.37 ( 62%)   6.62 ( 75%)  13.99 ( 67%)  1266M ( 68%)
 phase lang. deferred               :   2.70 ( 23%)   1.79 ( 20%)   4.49 ( 22%)   457M ( 25%)
 phase opt and generate             :   1.91 ( 16%)   0.43 (  5%)   2.35 ( 11%)   127M (  7%)
 |name lookup                       :   1.94 ( 16%)   1.51 ( 17%)   3.31 ( 16%)    43M (  2%)
 |overload resolution               :   2.96 ( 25%)   2.30 ( 26%)   5.41 ( 26%)   485M ( 26%)
 garbage collection                 :   1.58 ( 13%)   0.00 (  0%)   1.58 (  8%)     0  (  0%)
 dump files                         :   0.09 (  1%)   0.03 (  0%)   0.14 (  1%)     0  (  0%)
 callgraph construction             :   0.25 (  2%)   0.01 (  0%)   0.26 (  1%)    14M (  1%)
 callgraph optimization             :   0.02 (  0%)   0.03 (  0%)   0.06 (  0%)     0  (  0%)
 callgraph ipa passes               :   0.08 (  1%)   0.07 (  1%)   0.15 (  1%)  7973k (  0%)
 ipa dead code removal              :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 ipa inlining heuristics            :   0.01 (  0%)   0.01 (  0%)   0.01 (  0%)   312  (  0%)
 cfg cleanup                        :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)    12k (  0%)
 df scan insns                      :   0.03 (  0%)   0.00 (  0%)   0.03 (  0%)   111k (  0%)
 df live regs                       :   0.01 (  0%)   0.01 (  0%)   0.03 (  0%)     0  (  0%)
 df reg dead/unused notes           :   0.01 (  0%)   0.02 (  0%)   0.01 (  0%)   947k (  0%)
 register information               :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 rebuild jump labels                :   0.00 (  0%)   0.01 (  0%)   0.02 (  0%)    96  (  0%)
 preprocessing                      :   0.69 (  6%)   1.19 ( 13%)   2.04 ( 10%)    89M (  5%)
 parser (global)                    :   1.05 (  9%)   1.39 ( 16%)   2.25 ( 11%)   267M ( 14%)
 parser struct body                 :   0.60 (  5%)   0.58 (  7%)   1.21 (  6%)   110M (  6%)
 parser enumerator list             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)   912k (  0%)
 parser function body               :   0.12 (  1%)   0.08 (  1%)   0.22 (  1%)  9592k (  1%)
 parser inl. func. body             :   0.57 (  5%)   0.44 (  5%)   1.08 (  5%)    79M (  4%)
 parser inl. meth. body             :   0.60 (  5%)   0.49 (  6%)   1.05 (  5%)    93M (  5%)
 template instantiation             :   5.41 ( 45%)   3.93 ( 44%)   9.25 ( 44%)  1059M ( 57%)
 constant expression evaluation     :   0.20 (  2%)   0.27 (  3%)   0.37 (  2%)    12M (  1%)
 tree gimplify                      :   0.00 (  0%)   0.01 (  0%)   0.03 (  0%)  8527k (  0%)
 tree eh                            :   0.03 (  0%)   0.01 (  0%)   0.01 (  0%)  1813k (  0%)
 tree CFG construction              :   0.01 (  0%)   0.01 (  0%)   0.00 (  0%)  3813k (  0%)
 tree CFG cleanup                   :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)  4400  (  0%)
 tree PHI insertion                 :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)   434k (  0%)
 tree SSA rewrite                   :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)  1520k (  0%)
 tree SSA other                     :   0.01 (  0%)   0.01 (  0%)   0.02 (  0%)   338k (  0%)
 tree operand scan                  :   0.02 (  0%)   0.01 (  0%)   0.01 (  0%)  3409k (  0%)
 tree switch lowering               :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)    19k (  0%)
 dominance computation              :   0.02 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 out of ssa                         :   0.03 (  0%)   0.01 (  0%)   0.04 (  0%)   249k (  0%)
 expand vars                        :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)   865k (  0%)
 expand                             :   0.04 (  0%)   0.01 (  0%)   0.07 (  0%)    12M (  1%)
 post expand cleanups               :   0.02 (  0%)   0.01 (  0%)   0.00 (  0%)  2065k (  0%)
 varconst                           :   0.09 (  1%)   0.04 (  0%)   0.19 (  1%)   348k (  0%)
 jump                               :   0.02 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 loop init                          :   0.02 (  0%)   0.00 (  0%)   0.01 (  0%)  1869k (  0%)
 mode switching                     :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 integrated RA                      :   0.09 (  1%)   0.06 (  1%)   0.17 (  1%)    57M (  3%)
 LRA non-specific                   :   0.02 (  0%)   0.04 (  0%)   0.12 (  1%)   393k (  0%)
 LRA virtuals elimination           :   0.00 (  0%)   0.01 (  0%)   0.05 (  0%)   985k (  0%)
 LRA reload inheritance             :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)   336  (  0%)
 LRA create live ranges             :   0.01 (  0%)   0.00 (  0%)   0.04 (  0%)    23k (  0%)
 LRA hard reg assignment            :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 reload                             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)    55k (  0%)
 thread pro- & epilogue             :   0.04 (  0%)   0.01 (  0%)   0.04 (  0%)  3906k (  0%)
 machine dep reorg                  :   0.00 (  0%)   0.01 (  0%)   0.01 (  0%)   281k (  0%)
 shorten branches                   :   0.01 (  0%)   0.01 (  0%)   0.04 (  0%)     0  (  0%)
 final                              :   0.04 (  0%)   0.04 (  0%)   0.03 (  0%)  4871k (  0%)
 symout                             :   0.02 (  0%)   0.00 (  0%)   0.08 (  0%)     0  (  0%)
 rest of compilation                :   0.14 (  1%)   0.04 (  0%)   0.09 (  0%)  6081k (  0%)
 repair loop structures             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 TOTAL                              :  11.98          8.84         20.83         1852M
[3/3] c++ main.o cuda.cuda.o -shared -L/home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/lib -lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda -ltorch -ltorch_python -L/home/mark/anaconda3/envs/pt/lib -lcudart -o to_gray_cuda_implicit_default.so
Compilation time: 21.74 seconds
Header count (approx): 0
Template instantiation time: 0.00s (0%)


===== Testing explicit_torch_h =====
[1/3] c++ -MMD -MF main.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_explicit_torch_h -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -std=c++17 -std=c++17 -ftime-report -c /mnt/data/Dev/test/pytorch_header_profile/explicit_torch_h/main.cpp -o main.o 

Time variable                                   usr           sys          wall           GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)  1423k (  0%)
 phase parsing                      :   7.01 ( 59%)   7.02 ( 76%)  14.03 ( 66%)  1266M ( 68%)
 phase lang. deferred               :   2.82 ( 24%)   1.82 ( 20%)   4.65 ( 22%)   457M ( 25%)
 phase opt and generate             :   1.99 ( 17%)   0.43 (  5%)   2.41 ( 11%)   127M (  7%)
 |name lookup                       :   1.71 ( 14%)   1.60 ( 17%)   3.31 ( 16%)    43M (  2%)
 |overload resolution               :   2.97 ( 25%)   2.30 ( 25%)   5.11 ( 24%)   485M ( 26%)
 garbage collection                 :   1.58 ( 13%)   0.00 (  0%)   1.59 (  8%)     0  (  0%)
 dump files                         :   0.08 (  1%)   0.07 (  1%)   0.20 (  1%)     0  (  0%)
 callgraph construction             :   0.27 (  2%)   0.04 (  0%)   0.26 (  1%)    14M (  1%)
 callgraph optimization             :   0.01 (  0%)   0.02 (  0%)   0.05 (  0%)     0  (  0%)
 callgraph ipa passes               :   0.05 (  0%)   0.11 (  1%)   0.15 (  1%)  7973k (  0%)
 ipa dead code removal              :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 ipa free lang data                 :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 cfg construction                   :   0.03 (  0%)   0.00 (  0%)   0.01 (  0%)   560k (  0%)
 cfg cleanup                        :   0.02 (  0%)   0.00 (  0%)   0.04 (  0%)    12k (  0%)
 trivially dead code                :   0.01 (  0%)   0.01 (  0%)   0.01 (  0%)     0  (  0%)
 df scan insns                      :   0.03 (  0%)   0.00 (  0%)   0.05 (  0%)   111k (  0%)
 df live regs                       :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)     0  (  0%)
 df reg dead/unused notes           :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)   947k (  0%)
 register information               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 rebuild jump labels                :   0.03 (  0%)   0.00 (  0%)   0.00 (  0%)    96  (  0%)
 preprocessing                      :   0.53 (  4%)   1.36 ( 15%)   2.01 ( 10%)    89M (  5%)
 parser (global)                    :   1.11 (  9%)   1.47 ( 16%)   2.32 ( 11%)   203M ( 11%)
 parser struct body                 :   0.65 (  5%)   0.58 (  6%)   1.32 (  6%)   174M (  9%)
 parser enumerator list             :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)   912k (  0%)
 parser function body               :   0.10 (  1%)   0.11 (  1%)   0.22 (  1%)  9592k (  1%)
 parser inl. func. body             :   0.54 (  5%)   0.38 (  4%)   1.06 (  5%)    79M (  4%)
 parser inl. meth. body             :   0.74 (  6%)   0.47 (  5%)   1.13 (  5%)    93M (  5%)
 template instantiation             :   5.14 ( 43%)   4.29 ( 46%)   9.33 ( 44%)  1059M ( 57%)
 constant expression evaluation     :   0.23 (  2%)   0.12 (  1%)   0.42 (  2%)    12M (  1%)
 inline parameters                  :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)   473k (  0%)
 tree gimplify                      :   0.01 (  0%)   0.00 (  0%)   0.03 (  0%)  8527k (  0%)
 tree eh                            :   0.00 (  0%)   0.01 (  0%)   0.04 (  0%)  1813k (  0%)
 tree CFG construction              :   0.00 (  0%)   0.01 (  0%)   0.01 (  0%)  3813k (  0%)
 tree CFG cleanup                   :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)  4400  (  0%)
 tree SSA rewrite                   :   0.01 (  0%)   0.02 (  0%)   0.01 (  0%)  1520k (  0%)
 tree SSA other                     :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)   338k (  0%)
 tree operand scan                  :   0.00 (  0%)   0.03 (  0%)   0.01 (  0%)  3409k (  0%)
 dominance computation              :   0.01 (  0%)   0.00 (  0%)   0.03 (  0%)     0  (  0%)
 out of ssa                         :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)   249k (  0%)
 expand vars                        :   0.03 (  0%)   0.00 (  0%)   0.00 (  0%)   865k (  0%)
 expand                             :   0.07 (  1%)   0.01 (  0%)   0.11 (  1%)    12M (  1%)
 post expand cleanups               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)  2065k (  0%)
 varconst                           :   0.04 (  0%)   0.06 (  1%)   0.07 (  0%)   348k (  0%)
 jump                               :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 loop init                          :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)  1869k (  0%)
 loop fini                          :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 integrated RA                      :   0.15 (  1%)   0.06 (  1%)   0.18 (  1%)    57M (  3%)
 LRA non-specific                   :   0.06 (  1%)   0.01 (  0%)   0.03 (  0%)   393k (  0%)
 LRA virtuals elimination           :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)   985k (  0%)
 LRA reload inheritance             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)   336  (  0%)
 LRA create live ranges             :   0.03 (  0%)   0.01 (  0%)   0.01 (  0%)    23k (  0%)
 LRA hard reg assignment            :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 reload                             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)    55k (  0%)
 thread pro- & epilogue             :   0.04 (  0%)   0.01 (  0%)   0.05 (  0%)  3906k (  0%)
 machine dep reorg                  :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)   281k (  0%)
 shorten branches                   :   0.01 (  0%)   0.01 (  0%)   0.01 (  0%)     0  (  0%)
 final                              :   0.02 (  0%)   0.01 (  0%)   0.09 (  0%)  4871k (  0%)
 symout                             :   0.02 (  0%)   0.00 (  0%)   0.07 (  0%)     0  (  0%)
 rest of compilation                :   0.12 (  1%)   0.06 (  1%)   0.17 (  1%)  6081k (  0%)
 unaccounted post reload            :   0.00 (  0%)   0.02 (  0%)   0.00 (  0%)     0  (  0%)
 unaccounted late compilation       :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     0  (  0%)
 TOTAL                              :  11.82          9.27         21.10         1852M
[2/3] /home/mark/anaconda3/envs/pt/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_explicit_torch_h -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_89,code=sm_89 --compiler-options '-fPIC' -arch=sm_89 -std=c++17 -c /mnt/data/Dev/test/pytorch_header_profile/explicit_torch_h/cuda.cu -o cuda.cuda.o 
[3/3] c++ main.o cuda.cuda.o -shared -L/home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/lib -lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda -ltorch -ltorch_python -L/home/mark/anaconda3/envs/pt/lib -lcudart -o to_gray_cuda_explicit_torch_h.so
Compilation time: 40.06 seconds
Header count (approx): 0
Template instantiation time: 0.00s (0%)


===== Testing minimal_includes =====
[1/3] /home/mark/anaconda3/envs/pt/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_minimal_includes -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_89,code=sm_89 --compiler-options '-fPIC' -arch=sm_89 -std=c++17 -c /mnt/data/Dev/test/pytorch_header_profile/minimal_includes/cuda.cu -o cuda.cuda.o 
[2/3] c++ -MMD -MF main.o.d -DTORCH_EXTENSION_NAME=to_gray_cuda_minimal_includes -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/TH -isystem /home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/include/THC -isystem /home/mark/anaconda3/envs/pt/include -isystem /home/mark/anaconda3/envs/pt/include/python3.10 -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -std=c++17 -std=c++17 -ftime-report -c /mnt/data/Dev/test/pytorch_header_profile/minimal_includes/main.cpp -o main.o 

Time variable                                   usr           sys          wall           GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)  1423k (  0%)
 phase parsing                      :   7.16 ( 60%)   6.91 ( 75%)  14.07 ( 67%)  1266M ( 68%)
 phase lang. deferred               :   2.77 ( 23%)   1.79 ( 20%)   4.56 ( 22%)   457M ( 25%)
 phase opt and generate             :   1.93 ( 16%)   0.47 (  5%)   2.40 ( 11%)   127M (  7%)
 |name lookup                       :   1.88 ( 16%)   1.45 ( 16%)   3.00 ( 14%)    43M (  2%)
 |overload resolution               :   3.06 ( 26%)   2.20 ( 24%)   5.08 ( 24%)   485M ( 26%)
 garbage collection                 :   1.57 ( 13%)   0.01 (  0%)   1.61 (  8%)     0  (  0%)
 dump files                         :   0.10 (  1%)   0.05 (  1%)   0.16 (  1%)     0  (  0%)
 callgraph construction             :   0.18 (  2%)   0.02 (  0%)   0.23 (  1%)    14M (  1%)
 callgraph optimization             :   0.03 (  0%)   0.03 (  0%)   0.03 (  0%)     0  (  0%)
 callgraph ipa passes               :   0.06 (  1%)   0.10 (  1%)   0.15 (  1%)  7973k (  0%)
 ipa inheritance graph              :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)   102k (  0%)
 ipa inlining heuristics            :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)   312  (  0%)
 ipa modref                         :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 cfg construction                   :   0.00 (  0%)   0.01 (  0%)   0.03 (  0%)   560k (  0%)
 trivially dead code                :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)     0  (  0%)
 df scan insns                      :   0.02 (  0%)   0.00 (  0%)   0.05 (  0%)   111k (  0%)
 df live regs                       :   0.04 (  0%)   0.00 (  0%)   0.03 (  0%)     0  (  0%)
 alias analysis                     :   0.01 (  0%)   0.01 (  0%)   0.01 (  0%)   370k (  0%)
 rebuild jump labels                :   0.00 (  0%)   0.01 (  0%)   0.01 (  0%)    96  (  0%)
 preprocessing                      :   0.65 (  5%)   1.14 ( 12%)   1.89 (  9%)    89M (  5%)
 parser (global)                    :   1.06 (  9%)   1.57 ( 17%)   2.43 ( 12%)   267M ( 14%)
 parser struct body                 :   0.66 (  6%)   0.55 (  6%)   1.16 (  6%)   110M (  6%)
 parser enumerator list             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)   912k (  0%)
 parser function body               :   0.15 (  1%)   0.11 (  1%)   0.28 (  1%)  9592k (  1%)
 parser inl. func. body             :   0.58 (  5%)   0.41 (  4%)   1.09 (  5%)    79M (  4%)
 parser inl. meth. body             :   0.64 (  5%)   0.64 (  7%)   1.17 (  6%)    93M (  5%)
 template instantiation             :   4.99 ( 42%)   3.91 ( 43%)   9.22 ( 44%)  1059M ( 57%)
 constant expression evaluation     :   0.38 (  3%)   0.21 (  2%)   0.39 (  2%)    12M (  1%)
 early inlining heuristics          :   0.00 (  0%)   0.01 (  0%)   0.00 (  0%)  7168  (  0%)
 inline parameters                  :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)   473k (  0%)
 integration                        :   0.02 (  0%)   0.00 (  0%)   0.00 (  0%)    94k (  0%)
 tree gimplify                      :   0.04 (  0%)   0.02 (  0%)   0.06 (  0%)  8527k (  0%)
 tree eh                            :   0.02 (  0%)   0.01 (  0%)   0.01 (  0%)  1813k (  0%)
 tree CFG construction              :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)  3813k (  0%)
 tree CFG cleanup                   :   0.04 (  0%)   0.01 (  0%)   0.03 (  0%)  4400  (  0%)
 tree SSA rewrite                   :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)  1520k (  0%)
 tree SSA other                     :   0.01 (  0%)   0.03 (  0%)   0.02 (  0%)   338k (  0%)
 tree operand scan                  :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)  3409k (  0%)
 tree switch lowering               :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)    19k (  0%)
 dominance computation              :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 out of ssa                         :   0.02 (  0%)   0.01 (  0%)   0.01 (  0%)   249k (  0%)
 expand                             :   0.06 (  1%)   0.01 (  0%)   0.04 (  0%)    12M (  1%)
 post expand cleanups               :   0.01 (  0%)   0.02 (  0%)   0.04 (  0%)  2065k (  0%)
 varconst                           :   0.06 (  1%)   0.12 (  1%)   0.18 (  1%)   348k (  0%)
 jump                               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 loop init                          :   0.01 (  0%)   0.01 (  0%)   0.01 (  0%)  1869k (  0%)
 mode switching                     :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 integrated RA                      :   0.17 (  1%)   0.04 (  0%)   0.20 (  1%)    57M (  3%)
 LRA non-specific                   :   0.05 (  0%)   0.01 (  0%)   0.03 (  0%)   393k (  0%)
 LRA virtuals elimination           :   0.00 (  0%)   0.01 (  0%)   0.02 (  0%)   985k (  0%)
 LRA reload inheritance             :   0.00 (  0%)   0.01 (  0%)   0.01 (  0%)   336  (  0%)
 LRA create live ranges             :   0.00 (  0%)   0.01 (  0%)   0.02 (  0%)    23k (  0%)
 LRA hard reg assignment            :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)     0  (  0%)
 reload                             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)    55k (  0%)
 thread pro- & epilogue             :   0.03 (  0%)   0.00 (  0%)   0.04 (  0%)  3906k (  0%)
 machine dep reorg                  :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)   281k (  0%)
 shorten branches                   :   0.00 (  0%)   0.01 (  0%)   0.06 (  0%)     0  (  0%)
 reg stack                          :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 final                              :   0.07 (  1%)   0.03 (  0%)   0.04 (  0%)  4871k (  0%)
 symout                             :   0.03 (  0%)   0.03 (  0%)   0.07 (  0%)     0  (  0%)
 initialize rtl                     :   0.00 (  0%)   0.01 (  0%)   0.01 (  0%)    12k (  0%)
 rest of compilation                :   0.08 (  1%)   0.07 (  1%)   0.17 (  1%)  6081k (  0%)
 unaccounted post reload            :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     0  (  0%)
 TOTAL                              :  11.86          9.17         21.04         1852M
[3/3] c++ main.o cuda.cuda.o -shared -L/home/mark/anaconda3/envs/pt/lib/python3.10/site-packages/torch/lib -lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda -ltorch -ltorch_python -L/home/mark/anaconda3/envs/pt/lib -lcudart -o to_gray_cuda_minimal_includes.so
Compilation time: 21.90 seconds
Header count (approx): 0
Template instantiation time: 0.00s (0%)


===== COMPARATIVE RESULTS =====
Header Combination   | Total Time (s)  | Header Count    | Template Time (s) | Template %
--------------------------------------------------------------------------------
implicit_default     | 21.74           | 0               | 0.00            | 0         
explicit_torch_h     | 40.06           | 0               | 0.00            | 0         
minimal_includes     | 21.90           | 0               | 0.00            | 0         


===== HEADER ANALYSIS =====

Analyzing implicit_default:

Analyzing explicit_torch_h:

Analyzing minimal_includes:


Conclusion: The results above show which header combinations lead to faster compilation times.
For production code, consider using the minimal includes approach and creating a precompiled header.
```