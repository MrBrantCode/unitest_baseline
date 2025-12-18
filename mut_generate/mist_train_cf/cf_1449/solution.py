"""
QUESTION:
Write a function named `factorial(n)` to calculate the factorial of a non-negative integer `n`, where the factorial of `n` is the product of all positive integers less than or equal to `n`, using recursion. The function should return the calculated factorial. The input `n` is a non-negative integer.
"""

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:  
        return n * factorial(n-1)