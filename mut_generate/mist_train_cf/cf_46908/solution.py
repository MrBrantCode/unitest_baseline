"""
QUESTION:
Write a function `sort_by_binary_and_value` that takes a list of integers as input and returns the sorted list in ascending order, first by the binary representation of the integers (most significant bit to least significant bit) and then by the integer values themselves. The function should use a stable sorting algorithm to preserve the original order of elements with equal binary keys.
"""

def sort_by_binary_and_value(nums):
    """
    Sorts a list of integers in ascending order, first by the binary representation of the integers 
    (most significant bit to least significant bit) and then by the integer values themselves.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    nums.sort()  # stable sort by integer value
    nums.sort(key=lambda x: bin(x)[2:])  # stable sort by binary representation
    return nums