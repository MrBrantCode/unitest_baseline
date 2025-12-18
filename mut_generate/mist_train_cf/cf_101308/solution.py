"""
QUESTION:
Calculate the total cost of an order with a potential 10% discount on the base price. Write a function called `calculate_total_cost` that takes in the base price of an item, a list of additional costs, and a boolean indicating whether the customer has a rewards card. The function should return the total cost of the order, with the discount applied only to the base price if the customer has a rewards card. The discount amount should be 10% of the base price.
"""

def calculate_total_cost(base_price, additional_costs, has_rewards_card):
    """
    Calculate the total cost of an order with a potential 10% discount on the base price.

    Args:
    base_price (float): The base price of the item.
    additional_costs (list): A list of additional costs.
    has_rewards_card (bool): A boolean indicating whether the customer has a rewards card.

    Returns:
    float: The total cost of the order.
    """
    # Calculate the total additional costs
    total_additional_costs = sum(additional_costs)
    
    # Apply the discount if the customer has a rewards card
    if has_rewards_card:
        # Calculate the discount amount
        discount_amount = base_price * 0.1
        # Subtract the discount amount from the base price
        base_price -= discount_amount
    
    # Calculate the total cost
    total_cost = base_price + total_additional_costs
    
    return total_cost