"""
QUESTION:
Implement a function `calculate_order_total` to calculate the total cost of a food order. The function should take two parameters: `menu_items` (a dictionary of food items with their prices) and `order` (a dictionary of ordered food items with their quantities). The function should return the total cost of the order.

Restrictions: 
- Assume that the keys in the `order` dictionary match the keys in the `menu_items` dictionary.
- If a food item is not found in the `menu_items` dictionary, ignore it in the calculation.
- The function should handle both integer and float prices and quantities.
"""

def calculate_order_total(menu_items, order):
    """
    Calculate the total cost of a food order.

    Args:
    - menu_items (dict): A dictionary of food items with their prices.
    - order (dict): A dictionary of ordered food items with their quantities.

    Returns:
    - total_cost (float): The total cost of the order.

    """
    total_cost = 0
    for item, quantity in order.items():
        if item in menu_items:
            total_cost += menu_items[item] * quantity
    return total_cost