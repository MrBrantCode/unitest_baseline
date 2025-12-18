"""
QUESTION:
Define a function `filter_ice_creams` that takes in a list of ice cream flavors, their corresponding prices, and dietary information, as well as a list of dietary restrictions to exclude. The function should return a list of tuples, each containing a string representing an ice cream flavor, a float representing its price, and a list of strings representing its dietary information, sorted by increasing price and excluding any flavors with the specified dietary restrictions. The input list of ice cream flavors should have at least 7 elements, each element being a tuple containing the flavor name, price, and dietary information.
"""

def filter_ice_creams(ice_creams, exclude_dietary):
    """
    This function filters a list of ice cream flavors based on their dietary information
    and returns a list of tuples, each containing the ice cream flavor, price, and 
    dietary information, sorted by increasing price.

    Args:
        ice_creams (list): A list of tuples, each containing the ice cream flavor, 
            price, and dietary information.
        exclude_dietary (list): A list of dietary restrictions to exclude from the 
            list of available flavors.

    Returns:
        list: A list of tuples, each containing the ice cream flavor, price, and 
            dietary information, sorted by increasing price and excluding any flavors 
            with the specified dietary restrictions.
    """
    return sorted([ice_cream for ice_cream in ice_creams if not any(dietary in exclude_dietary for dietary in ice_cream[2])], key=lambda x: x[1])