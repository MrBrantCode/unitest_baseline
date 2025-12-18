"""
QUESTION:
Create a function named `calculate_cart_total` that takes a list of dictionaries representing items in a cart. Each dictionary contains the keys "item", "cost", and "quantity". The function should return a dictionary containing the total cost of the items in the cart and the item with the highest cost per unit along with its quantity in the cart. The solution should have a time complexity of O(n), where n is the number of items in the cart, and a space complexity of O(1), without using built-in functions such as sum() or max().
"""

def calculate_cart_total(cart):
    """
    Calculate the total cost of items in a cart and find the item with the highest cost per unit.

    Args:
        cart (list): A list of dictionaries representing items in a cart.
            Each dictionary contains the keys "item", "cost", and "quantity".

    Returns:
        dict: A dictionary containing the total cost of the items in the cart and
            the item with the highest cost per unit along with its quantity in the cart.
    """
    if not cart:
        return {"total_cost": 0, "highest_cost_item": None}

    total_cost = 0
    highest_cost_item = cart[0]
    highest_cost = highest_cost_item["cost"] / highest_cost_item["quantity"]

    for item in cart:
        total_cost += item["cost"]
        cost_per_unit = item["cost"] / item["quantity"]
        if cost_per_unit > highest_cost:
            highest_cost = cost_per_unit
            highest_cost_item = item

    return {
        "total_cost": round(total_cost, 2),
        "highest_cost_item": {
            "item": highest_cost_item["item"],
            "cost_per_unit": round(highest_cost, 2),
            "quantity": highest_cost_item["quantity"]
        }
    }