"""
QUESTION:
Create a function named `total_weight` that calculates the total weight of groceries in a shopping basket. The function takes a list of dictionaries as input, where each dictionary represents a grocery item and contains the item's name, weight or total weight, and category. If an item has a "weight" key, it represents the weight of an individual item. If an item has a "total_weight" key instead, it represents the total weight of a packet of items. The function must handle both cases.
"""

def total_weight(groceries):
    total = 0.0
    for grocery in groceries:
        if "weight" in grocery:
            total += grocery["weight"]
        elif "total_weight" in grocery:
            total += grocery["total_weight"]
    return total