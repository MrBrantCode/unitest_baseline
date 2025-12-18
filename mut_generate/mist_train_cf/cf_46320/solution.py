"""
QUESTION:
Create a function `create_dict` that takes a list of sets as input and returns a dictionary where each set is a key and the corresponding value is the sum of the squares of the set's elements. Since sets are mutable, convert them to immutable `frozenset` to use as dictionary keys.
"""

def create_dict(sets):
    """
    Create a dictionary where each set is a key and the corresponding value is the sum of the squares of the set's elements.

    Args:
    sets (list): A list of sets.

    Returns:
    dict: A dictionary where each set is a key and the corresponding value is the sum of the squares of the set's elements.
    """
    return {frozenset(s): sum(i**2 for i in s) for s in sets}