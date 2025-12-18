"""
QUESTION:
Write a function `filter_and_sort_ice_creams` that takes two inputs: `ice_creams`, a list of tuples containing an ice cream flavor (string), price (float), and dietary information (list of strings); and `exclude_dietary`, a list of dietary restrictions to exclude. The function should return a sorted list of ice cream flavors and their prices, excluding any flavors with dietary restrictions specified in `exclude_dietary`. The list of ice cream flavors should be sorted in order of increasing price. Each tuple in the output list should contain the ice cream flavor, price, and dietary information. 

Restrictions: The input list `ice_creams` should have at least 7 elements, and each element should be a tuple containing a string, a float, and a list of strings.
"""

def filter_and_sort_ice_creams(ice_creams, exclude_dietary):
    """
    This function filters out ice cream flavors with certain dietary restrictions 
    and returns a sorted list of ice cream flavors and their prices.

    Args:
        ice_creams (list): A list of tuples containing an ice cream flavor, price, and dietary information.
        exclude_dietary (list): A list of dietary restrictions to exclude.

    Returns:
        list: A sorted list of ice cream flavors, prices, and dietary information.
    """
    return sorted([ice_cream for ice_cream in ice_creams if not any(dietary in exclude_dietary for dietary in ice_cream[2])], key=lambda x: x[1])