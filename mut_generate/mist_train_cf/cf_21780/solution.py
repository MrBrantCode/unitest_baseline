"""
QUESTION:
Write a function named count_divisible_by_three that takes a list of integers as input and returns the number of items in the list that are divisible by 3. The function should have a time complexity of O(n), where n is the length of the list.
"""

def count_divisible_by_three(numbers):
    """
    Returns the number of items in the list that are divisible by 3.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The number of items in the list that are divisible by 3.
    """
    count = 0
    for num in numbers:
        if num % 3 == 0:
            count += 1
    return count