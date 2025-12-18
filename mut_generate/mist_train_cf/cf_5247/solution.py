"""
QUESTION:
Define a function `calculate_sum_of_products` that calculates the sum of the products of the third-level elements in a nested list with up to three levels of nesting. Each element is a positive integer. Only consider elements at the third level of nesting.
"""

def calculate_sum_of_products(nested_list):
    """
    This function calculates the sum of the products of the third-level elements 
    in a nested list with up to three levels of nesting. Each element is a positive integer.

    Args:
        nested_list (list): A nested list with up to three levels of nesting.

    Returns:
        int: The sum of the products of the third-level elements.
    """
    sum_of_products = 0
    for sublist in nested_list:
        for inner_list in sublist:
            if isinstance(inner_list, list):
                for element in inner_list:
                    if isinstance(element, int) and element > 0:
                        sum_of_products += element
    return sum_of_products