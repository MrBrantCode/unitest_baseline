"""
QUESTION:
Write a function called `marginal_revenue` that takes in two parameters: `demand_curve` and `quantity`. `demand_curve` is a function that returns the price corresponding to a given quantity, and `quantity` is the current quantity sold. The function should return the marginal revenue at the given quantity, calculated as the difference in prices when the quantity is increased by 1.
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
    marginal_revenue = (quantity + 1) * next_price - quantity * current_price 
    return marginal_revenue