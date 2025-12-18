"""
QUESTION:
Write a function to determine the charge status based on a plan type and a value. The function should take two parameters: `plan` and `value`. If the plan is either "Pro" or "Standard" and the value is greater than 0, return "Charged". If the plan is "Lite" and the value is greater than 0, return "Charged". Otherwise, return "FOC".
"""

def entrance(plan, value):
    """
    Determine the charge status based on a plan type and a value.

    Args:
        plan (str): The plan type. It can be "Pro", "Standard", or "Lite".
        value (float): The value to check.

    Returns:
        str: The charge status. It can be "Charged" or "FOC".
    """
    if plan in ["Pro", "Standard", "Lite"] and value > 0:
        return "Charged"
    else:
        return "FOC"