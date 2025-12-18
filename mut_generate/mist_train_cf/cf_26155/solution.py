"""
QUESTION:
Create a function called `reverse_list` that takes a list of strings as input and returns a new list containing the input strings in reverse order. The function should not modify the original list.
"""

def reverse_list(input_list):
    """
    This function takes a list of strings as input and returns a new list containing the input strings in reverse order.
    
    Args:
        input_list (list): A list of strings.
    
    Returns:
        list: A new list containing the input strings in reverse order.
    """
    return input_list[::-1]