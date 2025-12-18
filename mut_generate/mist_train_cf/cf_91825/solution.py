"""
QUESTION:
Create a function `calculate_total_cost` that calculates the total cost of a meal including taxes and tips. The function should take three parameters: `meal_price`, `tax_rate`, and `tip_percentage`. The meal price should be a positive decimal value, and the tax rate and tip percentage should be decimal values between 0 and 1, inclusive. The function should return the total cost as a string with a dollar sign prefix, rounded to the nearest cent.
"""

def calculate_total_cost(meal_price, tax_rate, tip_percentage):
    """
    Calculate the total cost of a meal including taxes and tips.

    Args:
        meal_price (float): The price of the meal.
        tax_rate (float): The tax rate as a decimal value between 0 and 1, inclusive.
        tip_percentage (float): The tip percentage as a decimal value between 0 and 1, inclusive.

    Returns:
        str: The total cost as a string with a dollar sign prefix, rounded to the nearest cent.
    """
    # Calculate tax amount
    tax_amount = meal_price * tax_rate
    
    # Calculate tip amount
    tip_amount = meal_price * tip_percentage
    
    # Calculate total cost
    total_cost = meal_price + tax_amount + tip_amount
    
    # Round the total cost to the nearest cent
    total_cost = round(total_cost, 2)
    
    # Format the total cost as a string with a dollar sign prefix
    total_cost_str = '${:.2f}'.format(total_cost)
    
    return total_cost_str