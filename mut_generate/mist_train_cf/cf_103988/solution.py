"""
QUESTION:
Write a function `filter_numbers` that filters out numbers from a given list that are divisible by 3 and 5 but not by 2, and returns the sum of the filtered numbers. The function should ignore non-integer values in the list and handle the case where the input list is empty by returning a specific message.
"""

def filter_numbers(numbers):
    """Filters out numbers from a given list that are divisible by 3 and 5 but not by 2, 
    and returns the sum of the filtered numbers."""
    filtered_numbers = [num for num in numbers if isinstance(num, int) and num % 3 == 0 and num % 5 == 0 and num % 2 != 0]
    return sum(filtered_numbers) if filtered_numbers else "No numbers to filter."