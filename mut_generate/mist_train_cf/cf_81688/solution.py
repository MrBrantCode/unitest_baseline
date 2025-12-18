"""
QUESTION:
Move the last two elements of the given array to the front. The function should be named `move_last_two_to_front` and take an array as input, returning the modified array. The array is 1-indexed and has a length of at least 2.
"""

def move_last_two_to_front(arr):
    """
    Move the last two elements of the given array to the front.

    Args:
        arr (list): The input array.

    Returns:
        list: The modified array with the last two elements moved to the front.
    """
    return arr[-2:] + arr[:-2]