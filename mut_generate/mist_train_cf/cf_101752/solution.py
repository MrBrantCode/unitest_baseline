"""
QUESTION:
Write a function called `calculate_total_cost` that calculates the total cost of a Venti frappuccino order, taking into account a 10% discount on the base price if the customer has a rewards card. The function should accept the base price, extra shot price, whipped cream price, caramel drizzle price, and a boolean indicating whether the customer has a rewards card. The function should return the total cost rounded to two decimal places.
"""

def calculate_total_cost(base_price, extra_shot_price, whipped_cream_price, caramel_drizzle_price, has_rewards_card):
    """
    Calculates the total cost of a Venti frappuccino order, taking into account a 10% discount on the base price if the customer has a rewards card.

    Args:
        base_price (float): The base price of the Venti frappuccino.
        extra_shot_price (float): The price of an extra shot of espresso.
        whipped_cream_price (float): The price of whipped cream.
        caramel_drizzle_price (float): The price of caramel drizzle.
        has_rewards_card (bool): Whether the customer has a rewards card.

    Returns:
        float: The total cost of the order rounded to two decimal places.
    """
    total_cost = base_price + extra_shot_price + whipped_cream_price + caramel_drizzle_price
    if has_rewards_card:
        discount_amount = base_price * 0.1
        base_price -= discount_amount
        total_cost = base_price + extra_shot_price + whipped_cream_price + caramel_drizzle_price
    return round(total_cost, 2)