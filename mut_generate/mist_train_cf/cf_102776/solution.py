"""
QUESTION:
Write a function named `sum_recursive` that takes a list of numbers and its start and end indices, and returns the sum of the numbers in the list from the start index to the end index using a recursive approach. The function should recursively split the list into two halves and sum the numbers in each half.
"""

def sum_recursive(numbers, start, end):
    """
    This function calculates the sum of the numbers in the list from the start index to the end index using a recursive approach.

    Args:
        numbers (list): A list of numbers.
        start (int): The start index.
        end (int): The end index.

    Returns:
        int: The sum of the numbers in the list from the start index to the end index.
    """
    if start == end:
        return numbers[start]
    else:
        mid = (start + end) // 2
        left_sum = sum_recursive(numbers, start, mid)
        right_sum = sum_recursive(numbers, mid + 1, end)
        return left_sum + right_sum