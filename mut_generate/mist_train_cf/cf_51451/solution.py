"""
QUESTION:
Write a Python function `group_fruits_by_color` that takes a list of tuples as input, where each tuple contains the name of a fruit and its corresponding color. The function should return a dictionary where the keys are the colors and the values are lists of tuples containing the name of the fruit and its color, sorted by color. The input list does not need to be sorted. The function should handle the case where there are multiple fruits of the same color that are not consecutive in the input list.
"""

import itertools

def group_fruits_by_color(fruits):
    """
    This function groups a list of fruits by their color.

    Args:
    fruits (list): A list of tuples, where each tuple contains the name of a fruit and its corresponding color.

    Returns:
    dict: A dictionary where the keys are the colors and the values are lists of tuples containing the name of the fruit and its color.
    """
    
    # First, we sort the list of fruits by their color
    fruits.sort(key=lambda x: x[1])
    
    # We use itertools.groupby() to group the fruits by their color
    grouped_fruits = itertools.groupby(fruits, lambda x: x[1])
    
    # We convert the grouped fruits into a dictionary
    result = {key: list(group) for key, group in grouped_fruits}
    
    return result