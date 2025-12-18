"""
QUESTION:
Write a function called `kth_smallest` that takes a list of integers and a positive integer `k` as input, where `k` is less than or equal to the length of the list. The function should return the kth smallest number in the list.
"""

def kth_smallest(numbers, k):
    """
    Returns the kth smallest number in a list of integers.

    Args:
        numbers (list): A list of integers.
        k (int): A positive integer representing the position of the number to find.

    Returns:
        int: The kth smallest number in the list.

    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[k-1]