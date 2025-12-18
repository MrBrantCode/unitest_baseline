"""
QUESTION:
Write a function called `reverse_array` that takes an array as input and reverses its elements in-place, without using any built-in array reversal methods or additional memory allocation. The function should return the reversed array.
"""

def reverse_array(list):
    """
    Reverses the elements of an array in-place.

    Args:
    list (list): The input array to be reversed.

    Returns:
    list: The reversed array.
    """
    left = 0
    right = len(list) - 1
    
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    
    return list