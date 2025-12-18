"""
QUESTION:
Create a function `square_numeric_values` that takes a list as input and returns a new list containing the squares of the numeric values from the input list. The function should ignore non-numeric values and handle cases where the input list is empty. The function should be able to process a list with different types of numbers, such as integers and floats.
"""

def square_numeric_values(input_list):
    """
    This function takes a list as input, squares the numeric values, 
    and returns a new list containing these squares. Non-numeric values 
    are ignored, and the function handles empty input lists.

    Args:
        input_list (list): A list containing various data types.

    Returns:
        list: A new list containing the squares of numeric values from the input list.
    """
    new_list = []
    for i in input_list:
        try:
            new_list.append(i**2)
        except TypeError:
            continue
    return new_list