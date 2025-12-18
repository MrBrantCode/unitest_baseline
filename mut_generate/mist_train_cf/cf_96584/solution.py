"""
QUESTION:
Write a function `calculate_total_cost` that takes a JSON string with the following structure: 
`{"items": [...], "quantity": [...], "cost": [...]}` where "items" is a list of item names, "quantity" is a list of corresponding quantities, and "cost" is a list of corresponding costs. 
The function should parse the JSON string, store each element into a variable, calculate the total cost by multiplying the quantity of each item by its respective cost, and return the result.
"""

import json

def calculate_total_cost(json_data):
    # Parse JSON
    data = json.loads(json_data)
    
    # Store elements in variables
    items = data["items"]
    quantity = data["quantity"]
    cost = data["cost"]
    
    # Calculate total cost
    total_cost = sum(quantity[i] * cost[i] for i in range(len(items)))
    
    return total_cost