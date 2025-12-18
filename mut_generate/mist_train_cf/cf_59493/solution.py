"""
QUESTION:
Write a function `invert(array)` that takes an integer array as input and inverts the elements in-place such that the first element swaps positions with the last one, the second element with the second last one, and so forth. The function should achieve this with O(1) space complexity and O(n) time complexity, without using any additional data structures.
"""

def invert(array):
    """
    Inverts the elements in an integer array in-place.

    The function swaps the first element with the last one, the second element with the second last one, and so forth.
    It achieves this with O(1) space complexity and O(n) time complexity, without using any additional data structures.

    Args:
        array (list): The input integer array.

    Returns:
        list: The inverted array.
    """
    i = 0
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return array