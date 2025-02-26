# Profiling tools that might be helpful

1. export NINJA_STATUS="[%f/%t %o/s %es] "
2. extra_cflags=["-ftime-trace", "-std=c++17"]
3. pip install iwyu
4. os.environ["TORCH_COMPILE_DB"] = "1"
5. import cProfile; cProfile.run('import your_module', 'profile_output')
6. pip install line_profiler
7. extra_cflags=["-H", "-std=c++17", "-ftime-report"]
8. extra_cflags=["-std=c++17", "-ftemplate-backtrace-limit=0"]
9. extra_cflags=["-ftime-trace", "-std=c++17"]
