"""
QUESTION:
Write a function called `reverse_list` that takes a list as input and returns a new list with its elements in reverse order. You cannot use any built-in list manipulation functions or methods, such as `reverse()`. You can only use basic programming constructs like loops and conditional statements.
"""

def reverse_list(input_list):
    """
    This function takes a list as input and returns a new list with its elements in reverse order.

    Args:
        input_list (list): The input list to be reversed.

    Returns:
        list: A new list with the elements in reverse order.
    """
    # Initialize an empty list to store the reversed elements
    reversed_list = []

    # Iterate over the elements of the original list in reverse order
    for i in range(len(input_list) - 1, -1, -1):
        # Append each element to the reversed list
        reversed_list.append(input_list[i])

    # Return the reversed list
    return reversed_list