"""
QUESTION:
Implement a function `sum_of_natural_numbers(n)` that calculates the sum of the first n natural numbers. The function should return an error message if n is not an integer or if n is negative. The algorithm should have a time complexity of O(1) and should not use any loops or recursion. The function should be able to handle both positive and negative values of n, and should return 0 if n is 0.
"""

def sum_of_natural_numbers(n):
    if not isinstance(n, int):
        return "Error: n is not an integer"
    if n < 0:
        return "Error: n is negative"
    
    if n == 0:
        return 0
    else:
        return n * (n + 1) // 2