"""
QUESTION:
Write a function `sort_ice_creams` that takes a list of ice cream flavors and their corresponding prices and dietary information as input and sorts them in order of increasing price, while ensuring that no flavors with certain dietary restrictions are included. Each element in the input list should be a tuple containing a string representing an ice cream flavor, a float representing its price, and a list of strings representing its dietary information. The function should also take a separate list of dietary restrictions to exclude from the list of available flavors.
"""

def sort_ice_creams(ice_creams, exclude_dietary):
    """
    Sorts a list of ice cream flavors by price, excluding flavors with certain dietary restrictions.

    Args:
    ice_creams (list): A list of tuples containing ice cream flavor, price, and dietary information.
    exclude_dietary (list): A list of dietary restrictions to exclude from the list of available flavors.

    Returns:
    list: A sorted list of available flavors and their prices, along with their corresponding dietary information.
    """
    return sorted([ice_cream for ice_cream in ice_creams if not any(dietary in exclude_dietary for dietary in ice_cream[2])], key=lambda x: x[1])