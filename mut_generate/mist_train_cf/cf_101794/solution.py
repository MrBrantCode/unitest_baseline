"""
QUESTION:
Design a function `calculate_order_cost` that takes in the base price of a drink, prices of optional add-ons, and a boolean indicating whether the customer has a rewards card. The function should return the total cost of the order, applying a 10% discount to the base price if the customer has a rewards card. The discount should not be applied to the prices of the add-ons.
"""

def calculate_order_cost(base_price, add_on_prices, has_rewards_card):
    """
    Calculate the total cost of an order, applying a 10% discount to the base price if the customer has a rewards card.

    Args:
        base_price (float): The base price of the drink.
        add_on_prices (list of float): A list of prices of optional add-ons.
        has_rewards_card (bool): A boolean indicating whether the customer has a rewards card.

    Returns:
        float: The total cost of the order.
    """
    # Apply the discount if the customer has a rewards card
    if has_rewards_card:
        base_price *= 0.9  # Apply 10% discount

    # Calculate the total cost by adding the base price and add-on prices
    total_cost = base_price + sum(add_on_prices)

    return total_cost