"""
QUESTION:
Write a recursive function `f(x)` that calculates the `x`th element in the Fibonacci series and explain its time complexity. Implement memoization to improve the performance of the function.

Restrictions:
- `x` is a non-negative integer.
- The function should have a base case to handle `x` values of 0 and 1.
- The function should recursively call itself with `x-1` and `x-2` arguments.
- The function should use memoization to store and return the results of previous function calls.
"""

def f(x, memo={}):
    if x == 0 or x == 1:
        return 1
    if x not in memo:
        memo[x] = f(x-1, memo) + f(x-2, memo)
    return memo[x]