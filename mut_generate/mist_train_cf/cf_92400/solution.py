"""
QUESTION:
Create a function named `filter_even_greater_than_10` that takes a list of integers as input and returns a new list containing all elements from the input list that are even and greater than 10. The returned list should be sorted in descending order.
"""

def filter_even_greater_than_10(numbers):
    """
    Returns a new list containing all elements from the input list that are even and greater than 10, sorted in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing all even integers greater than 10, sorted in descending order.
    """
    return sorted([num for num in numbers if num % 2 == 0 and num > 10], reverse=True)