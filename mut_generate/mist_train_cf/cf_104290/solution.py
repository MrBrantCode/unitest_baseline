"""
QUESTION:
Write an iterative function `fun` that calculates the nth Fibonacci number. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function must not use recursion and must have a time complexity of O(n).
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