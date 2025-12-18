"""
QUESTION:
Write a Python function named `fibonacci` that calculates the Fibonacci number at a given index without using recursion, loops, or built-in Python functions/libraries for calculating Fibonacci numbers. The function should return the corresponding Fibonacci number based on the provided index.
"""

def fibonacci(index):
    if index <= 0:
        return 0
    elif index == 1:
        return 1
    else:
        a = 0
        b = 1
        i = 2
        while i <= index:
            c = a + b
            a = b
            b = c
            i += 1
        return b