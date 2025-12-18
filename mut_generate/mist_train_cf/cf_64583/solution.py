"""
QUESTION:
Write a Python function `product_of_elements` that calculates the product of all elements in a four-dimensional array (a list of lists of lists of lists). The function should work for any number of elements in the innermost lists, any number of inner lists within each three-dimensional list, and an arbitrary number of three-dimensional lists within the outer list. The function should also handle potential zeroes in the array.
"""

def product_of_elements(arr):
    """
    This function calculates the product of all elements in a four-dimensional array.
    
    Args:
        arr (list): A four-dimensional array (a list of lists of lists of lists).
    
    Returns:
        int: The product of all elements in the array.
    """
    
    # Define a generator function that flattens any n-dimensional array
    def flatten(lst):
        for el in lst:
            if isinstance(el, list):
                yield from flatten(el)
            else:
                yield el
    
    # Get the product by iterating over the flattened list
    product = 1
    for num in flatten(arr):
        product *= num
    return product