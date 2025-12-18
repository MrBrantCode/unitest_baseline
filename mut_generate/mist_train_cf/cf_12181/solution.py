"""
QUESTION:
Create a function called `filter_even_numbers` that takes a list of integers as input, filters out the even numbers, and returns them in descending order. The function should not take any other parameters besides the list of integers.
"""

def filter_even_numbers(numbers):
    """Filters out even numbers from the input list and returns them in descending order."""
    return sorted([num for num in numbers if num % 2 == 0], reverse=True)