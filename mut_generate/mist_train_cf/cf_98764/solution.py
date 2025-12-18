"""
QUESTION:
Write a Python function `marginal_revenue(demand_curve, quantity)` that calculates the marginal revenue given a demand curve function and a current quantity sold. The demand curve function takes quantity as input and returns the corresponding price. The function should return the marginal revenue at the given quantity.
"""

def marginal_revenue(demand_curve, quantity):
    """
    Calculates the marginal revenue given a demand curve and a current quantity sold.
    
    Parameters:
    demand_curve (function): A function that takes quantity as input and returns the corresponding price.
    quantity (float): The current quantity sold.
    
    Returns:
    float: The marginal revenue at the given quantity.
    """
    current_price = demand_curve(quantity)
    next_quantity = quantity + 1
    next_price = demand_curve(next_quantity)
    marginal_revenue = (next_price * next_quantity) - (current_price * quantity)
    return marginal_revenue