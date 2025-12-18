"""
QUESTION:
Create a function called `swap_variables` that takes two variables of any data type as input and returns the swapped values without using a third variable.
"""

def swap_variables(a, b):
    """
    This function swaps two variables without using a third variable.

    Args:
        a (any): The first variable to be swapped.
        b (any): The second variable to be swapped.

    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a + b 
    b = a[:len(a)-len(b)] 
    a = a[len(b):] 
    return a, b