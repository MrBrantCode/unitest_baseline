"""
QUESTION:
Write a Python function `marginal_revenue` that takes a demand curve function and a current quantity sold as input and returns the marginal revenue at the given quantity. The demand curve function should take quantity as input and return the corresponding price. The function should calculate the marginal revenue by finding the difference in price when the quantity is increased by 1.
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
    marginal_revenue = (demand_curve(quantity + 1) * (quantity + 1)) - (demand_curve(quantity) * quantity)
    return marginal_revenue