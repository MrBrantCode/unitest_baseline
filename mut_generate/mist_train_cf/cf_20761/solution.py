"""
QUESTION:
Implement a function `calculate_sum` that takes a list of numbers as input and returns the sum of all integers in the list, including integers within nested lists, while ignoring any non-integer elements.
"""

def calculate_sum(numbers):
    """
    Calculate the sum of all integers in the list, including integers within nested lists,
    while ignoring any non-integer elements.

    Args:
        numbers (list): A list of numbers that may contain nested lists.

    Returns:
        int: The sum of all integers in the list.
    """
    total_sum = 0
    for num in numbers:
        if isinstance(num, int):
            total_sum += num
        elif isinstance(num, list):
            total_sum += calculate_sum(num)
    return total_sum