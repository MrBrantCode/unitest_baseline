"""
QUESTION:
Create a function `calculate_cumulative_sum` that takes an array of integers as input. The function should calculate the cumulative sum by multiplying each non-negative integer by its 0-based index and summing the results. The function should return the cumulative sum.
"""

def calculate_cumulative_sum(array):
    return sum(index * number for index, number in enumerate(array) if number >= 0)