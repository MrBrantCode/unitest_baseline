"""
QUESTION:
Create a function `create_ascending_tuple` that takes a list of eight distinct integers as input and returns a tuple containing the same integers in ascending order.
"""

def create_ascending_tuple(num_list):
    """Takes a list of eight distinct integers as input and returns a tuple containing the same integers in ascending order."""
    
    # Sort the list in ascending order
    num_list.sort()

    # Convert the list to a tuple
    num_tuple = tuple(num_list)

    # Return the resulting tuple
    return num_tuple