"""
QUESTION:
Write a function named `calculate_total_cost` that takes a list of dictionaries as input, where each dictionary represents an item with keys "item", "cost", and "quantity". The function should calculate the total cost of all items in the cart and find the item with the highest cost per unit. The function should return the total cost and the item with the highest cost per unit as a dictionary with keys "item" and "cost". Do not use built-in functions such as sum(), max(), or similar functions that directly solve the problem.
"""

def calculate_total_cost(cart):
    total_cost = 0
    highest_cost_per_unit = {"item": "", "cost": 0}

    for item in cart:
        item_cost = item["cost"] * item["quantity"]
        total_cost += item_cost

        cost_per_unit = item["cost"]
        if cost_per_unit > highest_cost_per_unit["cost"]:
            highest_cost_per_unit["item"] = item["item"]
            highest_cost_per_unit["cost"] = cost_per_unit

    return total_cost, highest_cost_per_unit