"""
QUESTION:
Write a function called `remove_duplicates` that takes an array of integers as input, removes duplicates while preserving the original sequence, and returns the resulting array. The function should be time and space efficient to handle arrays with up to 10^6 integers.
"""

def remove_duplicates(arr):
    """
    Removes duplicates from an array of integers while preserving the original sequence.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The resulting array with duplicates removed.
    """
    return list(dict.fromkeys(arr))