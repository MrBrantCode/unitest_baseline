"""
QUESTION:
Create a function named `find_highest_pricing_plan` that takes a list of dictionaries representing pricing plans as input. Each dictionary should contain the keys "name", "price", and "duration". The function should return the plan with the highest price that has a minimum price of $15 and a duration of at least 1 year. If no plan satisfies these constraints, the function should return None.
"""

def find_highest_pricing_plan(plans):
    """
    This function finds the pricing plan with the highest price that has a minimum price of $15 and a duration of at least 1 year.

    Args:
        plans (list): A list of dictionaries representing pricing plans.

    Returns:
        dict: The plan with the highest price that satisfies the constraints, or None if no plan satisfies the constraints.
    """
    valid_plans = [plan for plan in plans if plan["price"] >= 15 and plan["duration"] >= 1]
    if not valid_plans:
        return None
    return max(valid_plans, key=lambda plan: plan["price"])