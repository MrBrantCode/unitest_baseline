"""
QUESTION:
Create a function called `calculate_budget` that calculates the total budget for a given gift category in a list of gifts. The function should take two parameters: a list of gifts and a category. Each gift is represented as a dictionary containing the keys "name", "category", and "price". The function should return the total budget for the specified category. 

The function should also be able to handle cases where the specified category does not exist in the list of gifts.
"""

def calculate_budget(gifts, category):
    """
    Calculate the total budget for a given gift category.

    Args:
        gifts (list): A list of gifts, where each gift is a dictionary containing "name", "category", and "price".
        category (str): The gift category to calculate the total budget for.

    Returns:
        float: The total budget for the specified category.
    """
    budget = 0
    for gift in gifts:
        if gift["category"] == category:
            budget += gift["price"]
    return budget