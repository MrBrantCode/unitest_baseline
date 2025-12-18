"""
QUESTION:
Write a function `closest_num` that finds the number in a given array `arr` that is closest to a given target number. The function should take two parameters: `arr` (a list of numbers) and `target` (the target number). It should return the number in `arr` with the smallest absolute difference to `target`.
"""

def closest_num(arr, target):
    """
    Finds the number in a given array that is closest to a given target number.

    Args:
        arr (list): A list of numbers.
        target (int): The target number.

    Returns:
        int: The number in `arr` with the smallest absolute difference to `target`.
    """
    return arr[min(range(len(arr)), key = lambda index: abs(arr[index]-target))]