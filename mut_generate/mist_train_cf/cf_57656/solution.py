"""
QUESTION:
Write an iterative version of the factorial function that takes an integer n as input and returns its factorial. The function should not use recursion.
"""

def factorial(n): 
    result = 1
    for i in range(2, n+1):
        result *= i
    return result