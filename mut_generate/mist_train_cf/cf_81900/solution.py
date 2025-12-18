"""
QUESTION:
Create a function `find_longest_fruit` that takes a list of fruit names as input and returns the fruit name with the maximum character length. The function should only return the first occurrence of the longest fruit name if there are multiple fruit names with the same maximum length.
"""

def find_longest_fruit(fruit_names):
    """
    This function finds the fruit name with the maximum character length in a given list.

    Args:
        fruit_names (list): A list of fruit names.

    Returns:
        str: The fruit name with the maximum character length.
    """
    max_length_fruit = max(fruit_names, key=len)
    return max_length_fruit