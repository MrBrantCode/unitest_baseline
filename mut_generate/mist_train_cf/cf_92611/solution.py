"""
QUESTION:
Write a function `compute_sum` that takes a list of integers as input and returns the sum of all integers in the list using a for loop.
"""

def compute_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum