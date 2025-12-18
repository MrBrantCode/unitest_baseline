"""
QUESTION:
Write a function named `calculate_special_sum` that takes a list of integers as input and returns the sum of every fourth element in the list, skipping elements in a specific pattern. The pattern starts by skipping 3 elements, then 5 elements, then 7 elements, and so on, incrementing the skip count by 2 in each iteration.
"""

def calculate_special_sum(arr):
    """
    This function calculates the sum of every fourth element in the list, 
    skipping elements in a specific pattern.

    Args:
    arr (list): A list of integers.

    Returns:
    int: The sum of every fourth element in the list.
    """
    index = 0
    skip = 3
    total_sum = 0

    while index < len(arr):
        total_sum += arr[index]
        index += skip
        skip += 2

    return total_sum