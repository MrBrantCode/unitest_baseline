"""
QUESTION:
Create a function `calculate_total_cost` that takes a dictionary of items and their prices as input. The function should calculate the total cost of all items in the dictionary, excluding any items with prices greater than 1000. The total cost should be rounded to the nearest whole number. Assume that the input dictionary contains item names as keys and their corresponding prices as values.
"""

def calculate_total_cost(items):
    """
    Calculate the total cost of all items in the dictionary, excluding any items with prices greater than 1000.
    
    Args:
        items (dict): A dictionary containing item names as keys and their corresponding prices as values.
    
    Returns:
        int: The total cost rounded to the nearest whole number.
    """
    total_cost = sum(price for price in items.values() if price <= 1000)
    return round(total_cost)