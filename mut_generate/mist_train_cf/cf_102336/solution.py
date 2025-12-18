"""
QUESTION:
Compute the factorial of a given positive integer less than or equal to 100 using a recursive algorithm. The function should be named `factorial(n)` and the time complexity should be less than O(n^2).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)