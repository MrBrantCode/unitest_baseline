"""
QUESTION:
Write an iterative function `fun` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The function should not use recursion. Analyze the time complexity of the function.
"""

def fun(n):
    a = 0
    b = 1
    for _ in range(n):
        temp = a
        a = b
        b = temp + b
    return a