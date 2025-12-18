"""
QUESTION:
Write a function named `find_difference` that calculates the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. Implement this function using recursion and without using any built-in Python functions or libraries.
"""

def find_difference(n):
    # Base case
    if n == 1:
        return 0
    else:
        # Recursive call
        return n*n*n + find_difference(n-1) - n*(n+1)/2