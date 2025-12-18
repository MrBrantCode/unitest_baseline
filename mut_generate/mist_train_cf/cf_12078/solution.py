"""
QUESTION:
Create a function `replace_x_with_y` that takes a list as input and returns a new list where all instances of 'x' are replaced with 'y', maintaining the original order of elements. The input list can contain any type of elements, including integers and strings.
"""

def replace_x_with_y(input_list):
    """
    Replaces all instances of 'x' with 'y' in a given list.
    
    Args:
        input_list (list): The input list that may contain 'x' to be replaced.
    
    Returns:
        list: A new list with all instances of 'x' replaced with 'y'.
    """
    return ['y' if element == 'x' else element for element in input_list]