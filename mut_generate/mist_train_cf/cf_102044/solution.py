"""
QUESTION:
Create a function `reverse_list_copy` that takes a list as input and returns a new list containing the same elements, but in reverse order, without using any built-in list methods or functions for reversing or copying.
"""

def reverse_list_copy(input_list):
    """
    This function creates a new list containing the same elements as the input list, 
    but in reverse order, without using any built-in list methods or functions for 
    reversing or copying.

    Args:
        input_list (list): The list to be reversed and copied.

    Returns:
        list: A new list containing the same elements as the input list, but in reverse order.
    """

    # Create an empty list to store the reversed copy
    reversed_copy = []

    # Iterate through the original list in reverse order
    for i in range(len(input_list)-1, -1, -1):
        # Append each element to the reversed copy list
        reversed_copy.append(input_list[i])

    # Return the reversed copy list
    return reversed_copy