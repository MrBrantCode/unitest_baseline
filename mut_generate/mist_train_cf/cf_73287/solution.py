"""
QUESTION:
Implement a function called `product_of_list_elements` that calculates the product of all elements in a given list using a while loop. The function should take a list of integers as input and return the product of its elements. The input list can be of any length, including zero, and can contain any integer values.
"""

def product_of_list_elements(num_list):
    """
    Calculate the product of all elements in a given list using a while loop.

    Args:
        num_list (list): A list of integers.

    Returns:
        int: The product of the list elements.
    """
    product = 1
    index = 0

    while index < len(num_list):
        product *= num_list[index]
        index += 1

    return product