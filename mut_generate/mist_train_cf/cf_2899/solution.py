"""
QUESTION:
Implement a function `calculate_total_cost` that calculates the total cost of items in a shopping cart after applying any applicable discounts or promotions. The function should take a list of items in the cart, where each item is a dictionary containing the item's price and any applicable discounts or promotions, and return the total cost. The discounts or promotions should be represented as a percentage off the item's price.
"""

def calculate_total_cost(cart):
    """
    Calculate the total cost of items in a shopping cart after applying any applicable discounts or promotions.

    Args:
        cart (list): A list of items in the cart, where each item is a dictionary containing the item's price and any applicable discounts or promotions.

    Returns:
        float: The total cost of items in the cart.
    """
    total_cost = 0
    for item in cart:
        price = item['price']
        discount = item.get('discount', 0)
        total_cost += price * (1 - discount / 100)
    return total_cost