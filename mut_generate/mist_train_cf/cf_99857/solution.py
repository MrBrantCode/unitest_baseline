"""
QUESTION:
Write a function called `find_longest_river` that takes a dictionary of rivers and their lengths as input and returns the name of the longest river. The dictionary keys represent the names of the rivers and the values represent their lengths in kilometers.
"""

def find_longest_river(rivers):
    """
    This function takes a dictionary of rivers and their lengths as input and returns the name of the longest river.

    Parameters:
    rivers (dict): A dictionary where keys are river names and values are river lengths in kilometers.

    Returns:
    str: The name of the longest river.
    """
    return max(rivers, key=rivers.get)