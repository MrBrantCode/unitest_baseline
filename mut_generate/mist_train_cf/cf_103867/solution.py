"""
QUESTION:
Write a function `get_highest_plan` that takes a list of pricing plans as input, where each plan is a dictionary with 'name' and 'price' keys. The function should return the plan with the highest price that is greater than or equal to $15.
"""

def get_highest_plan(plans):
    """
    Returns the plan with the highest price that is greater than or equal to $15.

    Args:
    plans (list): A list of pricing plans, where each plan is a dictionary with 'name' and 'price' keys.

    Returns:
    dict: The plan with the highest price that is greater than or equal to $15.
    """
    return max((plan for plan in plans if plan['price'] >= 15), key=lambda x: x['price'], default=None)