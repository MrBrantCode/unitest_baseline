"""
QUESTION:
Write a function `common_elements` that takes two lists of strings as input and returns a list of elements that appear in both input lists, considering case sensitivity. If no elements match exactly due to case sensitivity, modify the function to ignore case sensitivity by converting all strings to lower case before comparison.
"""

def common_elements(list1, list2):
    """Returns a list of elements that appear in both input lists, ignoring case sensitivity."""
    return [x for x in list1 if x.lower() in [y.lower() for y in list2]]