"""
QUESTION:
Create a recursive function named `factorial(n)` that takes a non-negative integer `n` as input and returns the factorial of `n`. The function should handle the base case where `n` equals 0 and make recursive calls with decreasing values of `n` until it reaches the base case.
"""

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1)  