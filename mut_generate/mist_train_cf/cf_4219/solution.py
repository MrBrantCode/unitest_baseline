"""
QUESTION:
Write a function to swap the values of two variables in a single line of code, without using temporary variables, and capable of handling variables with different data types. The function should take two parameters and return the swapped values. The function should not have any restrictions on the data types of the input parameters.
"""

def swap_values(a, b):
    """
    Swap the values of two variables in a single line of code.

    This function takes two parameters of any data type, swaps their values, 
    and returns the swapped values.

    Args:
        a: The first variable.
        b: The second variable.

    Returns:
        tuple: A tuple containing the swapped values.
    """
    return b, a