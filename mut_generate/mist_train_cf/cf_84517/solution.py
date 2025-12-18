"""
QUESTION:
Implement the `factorial` function using tail recursion and an accumulator, where `n` is the number for which to calculate the factorial and `acc` is the accumulator with a default value of 1. The function should calculate the factorial of a given number and return the result. The function should not rely on Python's interpreter-level optimization of tail recursion, and it should be aware of the potential for a `RecursionError` with large inputs due to Python's maximum recursion depth.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n-1, n*acc)