"""
QUESTION:
Write a function `kth_smallest(numbers, k)` that takes a list of integers `numbers` and a positive integer `k` as input, where `k` is less than or equal to the length of `numbers`, and returns the kth smallest number from the list.
"""

def kth_smallest(numbers, k):
    """
    Returns the kth smallest number from a list of integers.

    Args:
        numbers (list): A list of integers.
        k (int): A positive integer representing the kth smallest number to find.

    Returns:
        int: The kth smallest number in the list.
    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[k-1]