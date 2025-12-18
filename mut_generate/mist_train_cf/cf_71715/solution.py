"""
QUESTION:
Write a function called `get_element_at_index` that takes a list and an index as input, and returns the element at that index if it exists. If the index is out of range, the function should handle the error and return a specific error message instead of raising an IndexError.
"""

def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "IndexError: list index out of range"