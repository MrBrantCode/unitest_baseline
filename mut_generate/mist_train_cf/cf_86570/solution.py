"""
QUESTION:
Write a function named `calculate_average` that takes a list of floating-point numbers and returns their average. Use type hints to specify the expected types of the function parameters and return value.
"""

def calculate_average(numbers: list[float]) -> float:
    total = sum(numbers)
    return total / len(numbers)