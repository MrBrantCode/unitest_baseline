"""
QUESTION:
Write a Python function named `find_mutual_elements` that takes two lists as input and returns a set of elements common to both lists. The function should handle lists with repeated and unique elements.
"""

def find_mutual_elements(list1, list2):
    """Return a set of elements common to both input lists."""
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)