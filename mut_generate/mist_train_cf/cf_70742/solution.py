"""
QUESTION:
Write a function named `recursive_function` that can potentially cause a stack overflow error. Implement a recursive function in Python that leads to a stack overflow and discuss ways to optimize it to avoid the error. The function should not have a proper base case to cause an infinite number of recursive calls.
"""

def recursive_function(n):
    if n == 0:
        return n
    else:
        recursive_function(n+1)