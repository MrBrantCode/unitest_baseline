"""
QUESTION:
Write a function `fibonacci(n, depth=1)` that calculates the `n-th` Fibonacci number and returns the result along with the maximum recursion depth. The function should use recursion to compute the Fibonacci sequence, and the recursion depth should be tracked. The base case for recursion is when `n` is less than or equal to 1, in which case the function returns `n` and the current recursion depth.
"""

def entance(n, depth=1):
    if n <= 1:
        return n, depth
    else:
        fib_n_minus_1, depth_1 = entance(n-1, depth + 1)
        fib_n_minus_2, depth_2 = entance(n-2, depth + 1)
        return fib_n_minus_1 + fib_n_minus_2, max(depth_1, depth_2)