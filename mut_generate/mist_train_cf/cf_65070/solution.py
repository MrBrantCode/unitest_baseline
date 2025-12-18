"""
QUESTION:
Create a function called `double_vector` that takes a vector of integers as input and returns a new vector where each element from the input vector is multiplied by 2. The function should handle vectors of any size.
"""

def double_vector(vector):
    """
    This function takes a list of integers as input, doubles each integer, 
    and returns the resulting list.

    Args:
    vector (list): A list of integers.

    Returns:
    list: A new list with each integer from the input list doubled.
    """
    return [x * 2 for x in vector]