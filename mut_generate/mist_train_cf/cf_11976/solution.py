"""
QUESTION:
Create a function named `remove_and_sort` that takes a list of integers as input. If the list contains at least 5 elements, remove the first item and add it to the `removed_numbers` list, then sort the original list in descending order.
"""

def remove_and_sort(numbers):
    """
    If the list contains at least 5 elements, remove the first item and add it to the removed_numbers list, 
    then sort the original list in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The modified list of integers.
        list: A list of removed numbers.
    """
    removed_numbers = []
    if len(numbers) >= 5:
        removed_numbers.append(numbers.pop(0))
        numbers.sort(reverse=True)
    return numbers, removed_numbers