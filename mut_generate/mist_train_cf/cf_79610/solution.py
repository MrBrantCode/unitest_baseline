"""
QUESTION:
Determine the data type of elements in a given set. 

Write a function `get_data_type` that takes a set of elements as input and returns the data type of the elements in the set. Assume the set contains elements of the same data type.
"""

def get_data_type(input_set):
    """
    This function determines the data type of elements in a given set.

    Args:
        input_set (set): A set of elements of the same data type.

    Returns:
        type: The data type of the elements in the set.
    """
    return type(next(iter(input_set)))