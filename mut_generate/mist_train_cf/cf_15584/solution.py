"""
QUESTION:
Create a function called 'fruit_color_pairs' that takes in two lists, 'fruits' and 'colors', and returns a list of objects where each object contains a key-value pair representing a fruit and its color. The key should be the fruit name and the value should be its corresponding color. The function should assume that the input lists are of the same length.
"""

def fruit_color_pairs(fruits, colors):
    """
    This function takes in two lists, 'fruits' and 'colors', 
    and returns a list of dictionaries where each dictionary contains 
    a key-value pair representing a fruit and its color.

    Args:
        fruits (list): A list of fruit names.
        colors (list): A list of fruit colors.

    Returns:
        list: A list of dictionaries where each dictionary contains a fruit-color pair.
    """
    return [{fruit: color} for fruit, color in zip(fruits, colors)]