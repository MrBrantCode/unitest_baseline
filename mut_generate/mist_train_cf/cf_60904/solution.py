"""
QUESTION:
Create a Python function named `factorial` to calculate the factorial of a given number using recursion. The function should take one positive integer argument and return its factorial. The function must use recursion to calculate the factorial.
"""

def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n==1:       
       return n
    else:
       return n * factorial(n-1)