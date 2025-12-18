"""
QUESTION:
Write a function called `flatten_list` that takes a two-dimensional list as input and returns a one-dimensional list with no duplicate elements. The input list contains integers and may have varying sub-list lengths. The function should preserve the original order of elements.
"""

def flatten_list(lst):
    seen = set()
    return [element for sublist in lst for element in sublist if not (element in seen or seen.add(element))]