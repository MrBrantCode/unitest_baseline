"""
QUESTION:
Create a function called `total_cost` that calculates the total cost of items in a cart. The function takes a list of dictionaries as input, where each dictionary represents an item and contains the keys "item" and "cost". The "item" key stores the name of the item and the "cost" key stores the price of the item. Return the total cost of all items.
"""

def total_cost(items):
    total = 0
    for item in items:
        total += item['cost']
    return total