"""
QUESTION:
Write a function `reverse_slice` that takes a list and an integer `n` as input, and returns the reversed slice of the list up to index `n` without using any built-in functions or methods that directly manipulate the list. The function should have a time complexity of O(n^2).
"""

def reverse_slice(my_list, n):
    """
    Reverses the slice of the list up to index n.

    Args:
        my_list (list): The input list.
        n (int): The index up to which the list should be reversed.

    Returns:
        list: The reversed slice of the list.
    """
    reversed_slice = []
    for i in range(n, -1, -1):
        reversed_slice.append(my_list[i])
    return reversed_slice