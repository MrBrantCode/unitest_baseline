"""
QUESTION:
Create a function `change_second_element` that takes a tuple as input and returns a new tuple where the second element is the sum of the first, third, and fourth elements of the input tuple.
"""

def change_second_element(input_tuple):
    """
    This function takes a tuple as input, calculates the sum of the first, third, and fourth elements, 
    and returns a new tuple where the second element is the calculated sum.

    Args:
        input_tuple (tuple): A tuple with at least four elements.

    Returns:
        tuple: A new tuple where the second element is the sum of the first, third, and fourth elements.
    """
    my_list = list(input_tuple)
    my_list[1] = my_list[0] + my_list[2] + my_list[3]
    return tuple(my_list)