"""
QUESTION:
Implement a function named `tribonacci` that takes an integer `n` and a dictionary `memo` as input. The function should return the nth term of the Tribonacci sequence, where `tribonacci(0) = 0`, `tribonacci(1) = 1`, `tribonacci(2) = 1`, `tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)` for `n > 2`, and `tribonacci(n) = tribonacci(n+3) - tribonacci(n+2) - tribonacci(n+1)` for `n < 0`. Implement the function using dynamic programming and memoization for optimization. The `memo` dictionary is used as a cache to store intermediate results. If the `memo` dictionary is not provided, it defaults to an empty dictionary.
"""

def tribonacci(n: int, memo = {}):
    """
    The Tribonacci sequence adheres to the following rules:
    tribonacci(0) = 0
    tribonacci(1) = 1
    tribonacci(2) = 1
    tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3) for n > 2
    tribonacci(n) = tribonacci(n+3) - tribonacci(n+2) - tribonacci(n+1) for n < 0

    Apply dynamic programming and cache intermediate results using memoization for optimization.
    """
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n < 0:
        result = tribonacci(n + 3, memo) - tribonacci(n + 2, memo) - tribonacci(n + 1, memo)
    else:
        result = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
        
    memo[n] = result
    return result