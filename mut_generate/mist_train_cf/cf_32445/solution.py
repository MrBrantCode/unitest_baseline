"""
QUESTION:
Create a function `calculate_average` that takes a list of numbers as input and returns the average of the numbers as a floating-point number. The function should handle an empty list by returning 0.0 to avoid division by zero.
"""

def calculate_average(numbers: list) -> float:
    if not numbers:
        return 0.0  # Return 0 if the list is empty to avoid division by zero
    return sum(numbers) / len(numbers)