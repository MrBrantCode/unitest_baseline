"""
QUESTION:
Implement an iterative function `fun(n)` to calculate the nth Fibonacci number, where `fun(n)` is the sum of the previous two values `fun(n-1)` and `fun(n-2)`. The function should handle negative values of `n` by returning 0 and should have a time complexity of O(n).
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