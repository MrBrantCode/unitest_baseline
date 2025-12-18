"""
QUESTION:
Write a function named `f` that iteratively calculates the nth Fibonacci number, where each number is the sum of the two preceding ones. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should not use recursion.
"""

def f(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a