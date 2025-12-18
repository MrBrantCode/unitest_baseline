"""
QUESTION:
Implement the `fun` function using an iterative approach to calculate the nth Fibonacci number, where `fun(n)` should return the nth Fibonacci number, and the input `n` is a non-negative integer. The function should have a time complexity of O(n) and should not use recursive calls.
"""

def fun(n):
    if n <= 1:
        return n
    else:
        prev1 = 0
        prev2 = 1
        current = None
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return current