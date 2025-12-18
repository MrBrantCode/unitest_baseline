"""
QUESTION:
Create a function called `count_element_occurrences` that takes a list of elements of different data types (e.g., integers, strings, tuples) as input and returns a dictionary-like object where the keys are the unique elements and the values are their respective occurrence counts. The function should handle hashable Python data types and should be implemented using the `collections.Counter` class.
"""

import collections

def count_element_occurrences(input_list):
    """
    Counts the occurrences of elements in a list, handling hashable Python data types.

    Args:
        input_list (list): A list of elements of different data types.

    Returns:
        collections.Counter: A dictionary-like object where keys are unique elements and values are their occurrence counts.
    """
    return collections.Counter(input_list)