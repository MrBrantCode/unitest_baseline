"""
QUESTION:
Write a function named `sum_of_squares_up_to` that calculates the sum of squares of numbers from 1 to `n` with a time complexity less than O(n). The input `n` is a positive integer.
"""

def sum_of_squares_up_to(n):
    return n*(n+1)*(2*n+1)//6