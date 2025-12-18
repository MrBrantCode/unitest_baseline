"""
QUESTION:
Create a function named `calculate_total_cost` that takes a list of dictionaries as input, where each dictionary represents an item in the cart with keys "item", "cost", and "quantity". The function should return a tuple containing the total cost of all items in the cart and the item with the highest cost per unit. The function should not use built-in functions such as sum() or max(). The input list can contain multiple instances of the same item, and the quantity of each item can be any positive integer.
"""

def calculate_total_cost(cart):
    """
    Calculate the total cost of all items in the cart and the item with the highest cost per unit.

    Args:
        cart (list): A list of dictionaries, where each dictionary represents an item in the cart with keys "item", "cost", and "quantity".

    Returns:
        tuple: A tuple containing the total cost of all items in the cart and the item with the highest cost per unit.
    """
    total_cost = 0
    highest_cost_per_unit = 0
    highest_cost_item = ""

    for item in cart:
        item_cost = item["cost"] * item["quantity"]
        total_cost += item_cost

        cost_per_unit = item["cost"]
        if item["quantity"] > 1:
            cost_per_unit /= item["quantity"]

        if cost_per_unit > highest_cost_per_unit:
            highest_cost_per_unit = cost_per_unit
            highest_cost_item = item["item"]

    return total_cost, highest_cost_item