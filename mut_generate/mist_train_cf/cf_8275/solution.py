"""
QUESTION:
Write a recursive function `fibonacci(n)` that takes an integer `n` as input and returns the `n`-th Fibonacci number without using memoization. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The function should not use any additional data structures for memoization. Provide a time complexity analysis for the solution.
"""

def entance(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return entance(n-1) + entance(n-2)