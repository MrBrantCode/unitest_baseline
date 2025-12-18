"""
QUESTION:
Write a function `compose_strings(names, blanks)` that takes two lists of strings `names` and `blanks` as input. Return a list of composed strings, where each string is created by replacing "__" in a string from `blanks` with the corresponding string from `names`. The output list should be sorted in alphabetical order. The function should have a time complexity of O(n log n), where n is the length of the input lists.
"""

def compose_strings(names, blanks):
    """
    This function takes two lists of strings as input. It returns a list of composed strings,
    where each string is created by replacing "__" in a string from `blanks` with the 
    corresponding string from `names`. The output list is sorted in alphabetical order.

    Args:
        names (list): A list of names.
        blanks (list): A list of strings with "__" placeholders.

    Returns:
        list: A list of composed strings sorted in alphabetical order.
    """
    return sorted([blank.replace("__", name) for name, blank in zip(names, blanks)])