"""
QUESTION:
Create a function named `calculate_total_cost` that takes a JSON string as input. The JSON string contains a list of items, each with a name, quantity, and cost. The function should calculate the total cost by multiplying the quantity of each item by its respective cost and return the result, excluding items with zero quantity or cost.
"""

import json

def calculate_total_cost(json_string):
    """
    Calculate the total cost from a given JSON string containing a list of items.
    
    Args:
    json_string (str): A JSON string containing a list of items.
    
    Returns:
    int: The total cost of all items in the JSON string, excluding items with zero quantity or cost.
    """
    data = json.loads(json_string)
    total_cost = sum(item['quantity'] * item['cost'] for item in data['items'] if item['quantity'] > 0 and item['cost'] > 0)
    return total_cost