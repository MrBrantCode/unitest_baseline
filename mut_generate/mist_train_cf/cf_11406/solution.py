"""
QUESTION:
Create a function named `calculate_total_cost` that takes three parameters: `meal_price`, `tax_rate`, and `tip_percentage`. The `meal_price` should be a positive decimal value, and both `tax_rate` and `tip_percentage` should be decimal values between 0 and 1, inclusive. The function should calculate the total cost of the meal by adding the meal price, tax amount, and tip amount, round the result to the nearest cent, and return the total cost as a string with a dollar sign ('$') prefix.
"""

def calculate_total_cost(meal_price, tax_rate, tip_percentage):
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