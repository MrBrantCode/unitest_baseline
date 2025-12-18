"""
QUESTION:
Calculate the total cost of a list of items after applying individual discounts.

Write a function `calculate_total_cost` that takes a list of dictionaries as input, where each dictionary represents an item with keys 'price', 'quantity', and 'discount'. The function should return the total cost of all items after applying the discount to each item.

Restrictions: The input list can contain any number of items, and the items can be in any order. Each item's discount is applied to its price before calculating the total cost.
"""

def calculate_total_cost(items):
    """
    Calculate the total cost of a list of items after applying individual discounts.

    Args:
        items (list): A list of dictionaries, where each dictionary represents an item with keys 'price', 'quantity', and 'discount'.

    Returns:
        float: The total cost of all items after applying the discount to each item.
    """
    total_cost = 0
    for item in items:
        discount_price = item['price'] - (item['price'] * item['discount'])
        item_cost = discount_price * item['quantity']
        total_cost += item_cost
    return total_cost