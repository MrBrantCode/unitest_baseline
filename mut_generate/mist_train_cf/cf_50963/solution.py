"""
QUESTION:
Implement a function named `factorial(n)` that calculates the factorial of a non-negative integer `n` using recursion, without utilizing Python's built-in multiplication or division functions. The function should return the factorial of `n`.
"""

def factorial(n):
    def add(x, y):
        if y == 0:
            return x
        return add(x + 1, y - 1)
    
    def mult(x, y):
        if y == 0 or y == 1:
            return x
        return add(mult(x, y - 1), x)
    
    if n == 0 or n == 1: 
        return 1
    else:
        return mult(n, factorial(n - 1))