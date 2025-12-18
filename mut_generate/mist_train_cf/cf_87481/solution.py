"""
QUESTION:
Implement an iterative function `fun(n)` that calculates the nth Fibonacci number. The function should handle negative values of `n` by returning 0 and must have a time complexity of O(n).
"""

def fun(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b