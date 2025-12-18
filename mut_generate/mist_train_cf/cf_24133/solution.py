"""
QUESTION:
Write a function called `reverse_list` that takes a list of integers as input and returns a new list containing the same integers in reverse order, without using any built-in list reverse functions. The function should not modify the original list.
"""

def reverse_list(input_list):
    """
    This function takes a list of integers as input and returns a new list containing the same integers in reverse order.

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list containing the same integers in reverse order.
    """
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list