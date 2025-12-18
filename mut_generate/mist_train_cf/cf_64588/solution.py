"""
QUESTION:
Write a function `catalan_number(n)` to calculate the nth Catalan number, where n is a non-negative integer. The function should use memoization to optimize repeated calculations. Additionally, create a function `catalan_numbers(arg)` that can take either a single integer or a tuple of two integers representing a range, and returns the corresponding Catalan number(s). If the input is invalid, it should print an error message and return an empty list or the result of the single number calculation. The function should handle cases where the input is not an integer or the range is invalid.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def catalan_number(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    catalan = [0 for _ in range(n+1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n]