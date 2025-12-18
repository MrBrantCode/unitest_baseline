"""
QUESTION:
Write a function `calculate_cost` that calculates the total cost of purchasing a certain quantity of items. The function should take two parameters: `quantity` (the number of items to purchase) and `unit_price` (the price of a single item, defaulting to 2.00). The function should apply a 3% discount for every 20 items purchased. The function should return the total cost after discounts. The function should also validate the inputs, returning an error message if `quantity` is not a non-negative integer or if `unit_price` is not a non-negative float.
"""

def calculate_cost(quantity, unit_price=2.00):
    """
    Calculate the total cost of purchasing a certain quantity of items.

    Args:
    quantity (int): The number of items to purchase.
    unit_price (float, optional): The price of a single item. Defaults to 2.00.

    Returns:
    float: The total cost after discounts.
    """
    if not isinstance(quantity, int) or not isinstance(unit_price, float) or quantity < 0 or unit_price < 0:
        return "Invalid input"

    total_discount = 0
    total_cost = quantity * unit_price

    for x in range(20, quantity+1, 20):
        total_discount += (total_cost * 3) / 100
    
    net_cost = total_cost - total_discount

    return net_cost