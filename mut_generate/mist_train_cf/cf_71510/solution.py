"""
QUESTION:
Design a function `product_of_num` that calculates the product of all numerical entities contained within a given iterable, including nested set structures, lists, tuples, and disregarding non-numeric elements. The function should extract the imaginary component of complex numbers for inclusion in the product. 

The input iterable can contain any data types, including but not limited to strings, dictionaries, boolean values, custom objects, and None. The function should return a suitable error message if a mathematical exception occurs during the calculation. The function should efficiently handle large numbers and floating point precision issues.

The function should be able to process iterables recursively and return the product as a float value.
"""

def product_of_num(data):
    """
    This function calculates the product of all numerical entities 
    within a given iterable including nested structures.
    Non-numeric types, complex numbers' imaginary parts and None are ignored.

    Parameters:
        data (iterable): an iterable (e.g., list, tuple, set)

    Returns:
        float: the product of all numerical entities
    """

    # If data is empty, return 1 as the product of no numbers is 1.
    if not data:
        return 1

    prod = 1
    for item in data:
        # If item is another iterable (e.g., list, tuple, set) call function recursively
        if isinstance(item, (list, tuple, set)):
            prod *= product_of_num(item)
        elif isinstance(item, (int, float)):
            # If item is a number, multiply the current product by this number
            prod *= item
        elif isinstance(item, complex):
            # If item is a complex number, multiply the product by the imaginary part of the number
            prod *= item.imag
    return prod