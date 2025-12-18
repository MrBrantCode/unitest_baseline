"""
QUESTION:
Implement a function named `fun` that calculates the nth Fibonacci number using an iterative approach and determine its computational complexity. The function should take an integer `n` as input and return the nth Fibonacci number.
"""

def fun(n):
    a = 0
    b = 1
    for _ in range(n):
        temp = a
        a = b
        b = temp + b
    return a