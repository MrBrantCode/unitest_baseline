"""
QUESTION:
Write a Python function named `calculate_average` that takes a list of numbers as input and returns the average of all non-negative numbers in the list. If the input list contains no non-negative numbers, the function should return 0.
"""

def calculate_average(numbers):
    non_negative_numbers = [num for num in numbers if num >= 0]
    if non_negative_numbers:
        return sum(non_negative_numbers) / len(non_negative_numbers)
    else:
        return 0