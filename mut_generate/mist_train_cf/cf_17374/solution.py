"""
QUESTION:
Create a function called `composed_strings` that takes two lists `names` and `blanks` as input. The function should return a new list of strings where each string is a combination of a name from `names` and an element from `blanks`, with "__" replaced by the corresponding name. The returned list should be sorted in alphabetical order. The time complexity of the solution should be O(n log n), where n is the length of the input lists.
"""

def composed_strings(names, blanks):
    """
    Returns a new list of strings where each string is a combination of a name from `names` and an element from `blanks`, 
    with "__" replaced by the corresponding name. The returned list is sorted in alphabetical order.

    Args:
        names (list): A list of names.
        blanks (list): A list of strings with "__" as a placeholder.

    Returns:
        list: A list of composed strings sorted in alphabetical order.
    """
    return sorted([blank.replace("__", name) for name in names for blank in blanks])