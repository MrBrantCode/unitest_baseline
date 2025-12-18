"""
QUESTION:
Create a function named `calculate_total_cost` that takes a dictionary `shopping_list` where keys are item names and values are prices. The function should calculate the total cost of all items in the dictionary with prices less than or equal to $10, round the total cost to the nearest cent, and return it as a string with the dollar sign symbol included.
"""

def calculate_total_cost(shopping_list):
    """
    Calculate the total cost of all items in the dictionary with prices less than or equal to $10.

    Args:
        shopping_list (dict): A dictionary where keys are item names and values are prices.

    Returns:
        str: The total cost rounded to the nearest cent, prefixed with a dollar sign.
    """
    total_cost = sum(price for price in shopping_list.values() if price <= 10)
    return "${:.2f}".format(round(total_cost, 2))