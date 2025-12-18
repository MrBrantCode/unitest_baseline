"""
QUESTION:
Create a function `get_highest_price` that takes a list of dictionaries, where each dictionary represents a pricing plan with 'name' and 'price' keys, and returns the name of the plan with the highest price. The function should handle cases where the input list is empty, or where a dictionary is missing the 'price' key or has a 'price' value of None.
"""

def get_highest_price(plans):
    """
    Returns the name of the plan with the highest price.

    Args:
        plans (list): A list of dictionaries, where each dictionary represents a pricing plan with 'name' and 'price' keys.

    Returns:
        str: The name of the plan with the highest price.
    """
    highest_price = 0
    highest_plan = None
    for plan in plans:
        try:
            price = plan['price']
        except KeyError:
            print(f"There is no price key in {plan}")
            continue
        if price is None:
            print(f"There is no price for the plan {plan['name']}")
            continue
        if price > highest_price:
            highest_price = price
            highest_plan = plan['name']
    return highest_plan