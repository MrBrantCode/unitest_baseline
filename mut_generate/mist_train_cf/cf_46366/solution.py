"""
QUESTION:
Write a function called `sort_numbers` that takes a list of decimal numbers as input, removes non-numerical values and null values from the list, sorts the remaining numbers in descending order, and returns the sorted list. The function should handle large lists efficiently and not modify the original list.
"""

def sort_numbers(numbers):
    # Filter out invalid inputs: non-numerical values and null values
    valid_numbers = [n for n in numbers if isinstance(n, (int, float))]

    # Sort the valid numbers in descending order
    sorted_numbers = sorted(valid_numbers, reverse=True)

    return sorted_numbers