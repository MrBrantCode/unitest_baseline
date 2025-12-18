"""
QUESTION:
Write a function `calculate_average(numbers)` that takes a list of numbers (integers or floating-point numbers) as input and returns the average of those numbers. If the input list is empty, the function should return 0. The average should be calculated as the sum of all numbers divided by the total count of numbers.
"""

def entrance(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)