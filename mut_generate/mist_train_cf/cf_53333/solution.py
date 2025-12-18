"""
QUESTION:
Create a function `create_index_dict` that takes a tuple of integers as input and returns a dictionary where the integers are keys and their corresponding values are the indexes in the tuple. If an integer is even, its corresponding value should be the cube of the index, otherwise, it should be the square of the index.
"""

def create_index_dict(tup):
    """
    This function takes a tuple of integers as input and returns a dictionary 
    where the integers are keys and their corresponding values are the indexes 
    in the tuple. If an integer is even, its corresponding value should be 
    the cube of the index, otherwise, it should be the square of the index.

    Args:
        tup (tuple): A tuple of integers.

    Returns:
        dict: A dictionary with integers as keys and their corresponding indexes 
              in the tuple as values.
    """
    index_dict = {}
    for index, value in enumerate(tup):
        if value % 2 == 0:     # check if the number is even
            # if the number is even, cube the index
            index_dict[value] = index**3
        else:                 # else the number is odd
            # if number is odd, square the index
            index_dict[value] = index**2
    return index_dict