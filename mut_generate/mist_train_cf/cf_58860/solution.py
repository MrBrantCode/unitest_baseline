"""
QUESTION:
Create a function called `factorial(n)` that calculates the factorial of a given number `n` using recursion and memoization. The function should store the results of previously computed factorials in a cache (memo) to optimize its performance. Implement the function to minimize redundant calculations and reduce time complexity.
"""

def factorial(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    return memo.setdefault(n, n * factorial(n - 1, memo))