"""
QUESTION:
Write a function named `square_list_elements` that takes a list of numbers as input and returns a new list containing the square of each element in the input list.
"""

def square_list_elements(original_list):
    """
    This function takes a list of numbers as input and returns a new list containing 
    the square of each element in the input list.

    Args:
        original_list (list): A list of numbers.

    Returns:
        list: A new list containing the square of each element in the input list.
    """
    return [el**2 for el in original_list]