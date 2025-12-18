"""
QUESTION:
Write a function named `calculate_average` that takes a list of numbers as input and returns the average of the numbers. The function should handle the case where the input list is empty and return a default value (0) in that case.
"""

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0
    return average