"""
QUESTION:
Write a function named `calculate_sum_min_max` that calculates the sum, minimum, and maximum of a given list. The list may contain both integers and strings, and the function should exclude the strings while performing the calculations.
"""

def calculate_sum_min_max(lst):
    """Calculate the sum, minimum, and maximum of a given list, excluding strings."""
    
    # Filter out non-integer elements from the list
    numbers = [element for element in lst if isinstance(element, int)]
    
    # Calculate the sum, minimum, and maximum of the numbers
    sum_numbers = sum(numbers)
    min_number = min(numbers) if numbers else None  # Handle the case when the list is empty or contains only strings
    max_number = max(numbers) if numbers else None  # Handle the case when the list is empty or contains only strings
    
    return sum_numbers, min_number, max_number