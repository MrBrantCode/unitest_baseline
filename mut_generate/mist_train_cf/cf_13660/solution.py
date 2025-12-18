"""
QUESTION:
Write a function named `parse_json_and_calculate_total_cost` that takes a JSON string as input, parses it, and calculates the total cost by multiplying the quantity of each item by its respective cost. The JSON string contains the following structure: `{"items": [string], "quantity": [int], "cost": [float]}`. The function should return the total cost and print each item's details in the format "item: quantity x cost = item_total_cost". If the JSON string is invalid, the function should catch the error and print "Error parsing JSON data."
"""

import json

def parse_json_and_calculate_total_cost(json_data):
    """
    This function takes a JSON string, parses it, and calculates the total cost by multiplying the quantity of each item by its respective cost.
    
    Args:
    json_data (str): A JSON string containing the items, their quantities, and costs.
    
    Returns:
    float: The total cost of all items.
    """
    
    try:
        data = json.loads(json_data)
        
        items = data["items"]
        quantity = data["quantity"]
        cost = data["cost"]
        
        total_cost = 0
        for i in range(len(items)):
            item = items[i]
            item_quantity = quantity[i]
            item_cost = cost[i]
            item_total_cost = item_quantity * item_cost
            total_cost += item_total_cost
            
            print(f"{item}: {item_quantity} x {item_cost} = {item_total_cost}")
        
        print(f"Total cost: {total_cost}")
        return total_cost
    
    except json.JSONDecodeError:
        print("Error parsing JSON data.")
        return None