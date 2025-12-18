"""
QUESTION:
Write two functions, `get_beam_length(dimensions)` and `is_beam_size_valid(dimensions, percentage_limit)`, to analyze a piece of text describing a beam's dimensions. 

The function `get_beam_length(dimensions)` should take a list of dimensions for a beam with a rectangular profile and return its overall length. The overall length is the maximum value in the list of dimensions.

The function `is_beam_size_valid(dimensions, percentage_limit)` should take a list of dimensions for a beam with a rectangular profile and a percentage limit, and return True if the beam's dimensions are within the specified limit and False otherwise. The function should use the `get_beam_length(dimensions)` function to get the overall length and calculate the maximum allowable size for each dimension.

The dimensions and percentage limit should be passed as arguments to the functions. Assume the input list of dimensions only contains positive integers and the percentage limit is a positive integer.
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