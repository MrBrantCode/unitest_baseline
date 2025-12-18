"""
QUESTION:
Create a function `calculate_average` that takes a list of numbers as input and returns the average of the positive numbers in the list. The function should exclude any negative numbers from the calculation. If the input list is empty or contains only negative numbers, the function should return 0.
"""

from typing import List

def calculate_average(numbers: List[float]) -> float:
    positive_numbers = [num for num in numbers if num > 0]
    if not positive_numbers:
        return 0
    return sum(positive_numbers) / len(positive_numbers)