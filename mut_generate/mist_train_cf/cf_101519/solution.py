"""
QUESTION:
Write a Python function `get_beam_length(dimensions)` that takes a list of dimensions for a beam with a rectangular profile and returns its overall length, which is the maximum value in the list of dimensions. 

Additionally, create a function `is_beam_size_valid(dimensions, percentage_limit)` that takes a list of dimensions for a beam with a rectangular profile and a percentage limit, and returns True if the beam's dimensions are within the specified limit and False otherwise. The function should consider the overall length of the beam and the percentage limit to determine the maximum allowable size for each dimension.
"""

def get_beam_length(dimensions):
    """
    This function takes in a list of dimensions for a beam with a rectangular profile and returns its overall length.
    """
    length = max(dimensions)
    return length

def is_beam_size_valid(dimensions, percentage_limit):
    """
    This function takes in a list of dimensions for a beam with a rectangular profile and a percentage limit, and
    returns True if the beam's dimensions are within the specified limit and False otherwise.
    """
    length = get_beam_length(dimensions)
    max_size = length * percentage_limit / 100
    if all(size <= max_size for size in dimensions):
        return True
    else:
        return False