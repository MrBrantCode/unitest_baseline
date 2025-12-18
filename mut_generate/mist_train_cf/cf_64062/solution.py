"""
QUESTION:
Write a function `fibonacci(n, memo={})` that calculates the nth Fibonacci number using memoization to improve efficiency. The function should handle cases where n is in the memo dictionary, n is less than or equal to 2, and n is greater than 2 by recursively calling itself. The function should also store the computed values in the memo dictionary to avoid redundant computations. Note that this function is limited by Python's maximum recursion depth, which is usually set to 1000.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        solution = 1
    else:
        solution = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = solution
    return solution