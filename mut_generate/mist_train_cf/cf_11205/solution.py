"""
QUESTION:
Create a function named `update_tuple` that takes a tuple of three elements as input, modifies the second element to be the sum of the first and third elements, and returns the updated tuple. Note that tuples are immutable in Python, so the function should return a new tuple with the modification rather than modifying the original tuple.
"""

def update_tuple(t):
    """
    Updates the second element of a tuple to be the sum of the first and third elements.

    Args:
        t (tuple): A tuple of three elements.

    Returns:
        tuple: A new tuple with the second element updated.
    """
    # Convert tuple to a list
    my_list = list(t)

    # Modify the second element
    my_list[1] = my_list[0] + my_list[2]

    # Convert the list back to a tuple
    return tuple(my_list)