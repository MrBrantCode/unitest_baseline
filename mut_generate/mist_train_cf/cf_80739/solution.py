"""
QUESTION:
Write a function `total_sum` that calculates the sum of cubes of all numbers in a multi-dimensional array up to 5 levels deep. The function should recursively traverse the array, cube each integer, and sum the results.
"""

def total_sum(numbers):
    return sum(i**3 if isinstance(i, int) else total_sum(i) for i in numbers)