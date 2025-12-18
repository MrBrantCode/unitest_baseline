"""
QUESTION:
Write a Python function named `factorial_recursive` that calculates the factorial of a given non-negative integer `n` using recursion. The function should not take any additional parameters. Implement the function in a way that it can cause a stack overflow for large inputs. 

Note: The function should only handle non-negative integers and should not include any error checking for invalid inputs.
"""

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)