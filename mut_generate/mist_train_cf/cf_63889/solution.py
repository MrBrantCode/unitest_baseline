"""
QUESTION:
Create a function named `calculate_values` that takes a list of numbers as input and returns the maximum, minimum, and average values of the list. The function should use built-in Python functions to calculate the maximum and minimum values and handle the case where the list contains at least one element.
"""

def calculate_values(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    avg_value = sum(numbers) / len(numbers)
    
    return max_value, min_value, avg_value