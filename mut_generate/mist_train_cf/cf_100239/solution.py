"""
QUESTION:
Write a function `calculate_total_cost` that takes a JSON string containing a list of items with their prices and returns the total cost of these items. The JSON string has the format: {"items": [{"name": item_name, "price": item_price}, ...]}. The function should return a number representing the total cost.
"""

import json

def calculate_total_cost(json_string):
    """
    Calculate the total cost of items in a JSON string.

    Args:
        json_string (str): A JSON string containing a list of items with their prices.

    Returns:
        float: The total cost of the items.
    """
    data = json.loads(json_string)
    total_cost = sum(item['price'] for item in data['items'])
    return total_cost