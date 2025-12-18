"""
QUESTION:
Create a function named `most_frequent_number` that takes an array of integers as input and returns the integer that appears with the highest frequency in the array. The function should be able to handle any array of integers, including arrays with multiple integers that appear with the same highest frequency, in which case it can return any one of them.
"""

from collections import Counter

def most_frequent_number(arr):
    """
    This function takes an array of integers as input and returns the integer that appears with the highest frequency in the array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The integer that appears with the highest frequency in the array.
    """
    counter = Counter(arr)
    return counter.most_common(1)[0][0]