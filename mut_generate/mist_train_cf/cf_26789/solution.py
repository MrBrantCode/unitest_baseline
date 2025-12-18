"""
QUESTION:
Implement a class method `calculate_average` that takes a list of numbers as input and returns the average as a floating-point number rounded to two decimal places. The method should handle both integer and floating-point numbers and return 0.0 for an empty list.
"""

def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)