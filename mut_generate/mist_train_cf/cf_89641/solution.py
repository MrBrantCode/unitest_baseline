"""
QUESTION:
Create a function `calculate_total_cost` that takes a JSON string as input and returns the total cost of all items. The JSON string contains a list of items, each with 'name', 'quantity', and 'cost' keys. The function should multiply the 'quantity' of each item by its 'cost' and sum up the results, excluding any items with a 'quantity' or 'cost' of zero.
"""

import json

def calculate_total_cost(json_string):
    """
    Calculate the total cost of all items in the given JSON string.

    Args:
    json_string (str): A JSON string containing a list of items, each with 'name', 'quantity', and 'cost' keys.

    Returns:
    float: The total cost of all items.
    """
    data = json.loads(json_string)
    total_cost = sum(item['quantity'] * item['cost'] for item in data['items'] if item['quantity'] > 0 and item['cost'] > 0)
    return total_cost