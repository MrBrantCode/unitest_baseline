"""
QUESTION:
Write an iterative version of a recursive function in Python that can handle large data structures, considering that Python does not optimize tail recursion and has a limited recursion depth of 1000. The function should be able to calculate the factorial of a given number n.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result