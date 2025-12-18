"""
QUESTION:
Implement a function named `bench_one` that takes in `test_func`, `env`, `case`, and any additional arguments `*args` and `**vargs`. The function should execute `test_func` with the provided arguments and return the time taken by `test_func` to execute in seconds. The `env` and `case` parameters are used to specify the environment and test case, but their values are not used in the function's implementation. The function should be able to handle any type of `test_func` and its corresponding arguments.
"""

import time

def bench_one(test_func, env, case, *args, **vargs) -> float:
    start_time = time.time()
    test_func(*args, **vargs)
    end_time = time.time()
    return end_time - start_time