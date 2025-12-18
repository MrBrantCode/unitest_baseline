"""
QUESTION:
Calculate the total cost of a coffee order with a rewards card discount. The function should take the base price of the coffee, additional costs, and a boolean indicating whether a rewards card is present as input. The function should apply a 10% discount to the base price only if the rewards card is present and return the total cost of the order.
"""

def calculate_coffee_order(base_price, additional_costs, has_rewards_card):
    """
    Calculate the total cost of a coffee order with a rewards card discount.

    Args:
        base_price (float): The base price of the coffee.
        additional_costs (float): Additional costs such as extra shots, whipped cream, etc.
        has_rewards_card (bool): Whether the customer has a rewards card.

    Returns:
        float: The total cost of the coffee order.
    """
    if has_rewards_card:
        # Apply a 10% discount to the base price
        base_price *= 0.9
    
    # Calculate the total cost by adding the base price and additional costs
    total_cost = base_price + additional_costs
    
    return total_cost