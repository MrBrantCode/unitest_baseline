"""
QUESTION:
Create a function `calculate_total_cost` that takes three parameters: `meal_price`, `tax_rate`, and `tip_percentage`. The function should calculate the total cost of a meal including taxes and tips. The `meal_price` should be a positive decimal value, `tax_rate` and `tip_percentage` should be decimal values between 0 and 1, inclusive. The function should return the total cost as a string with a dollar sign prefix, rounded to the nearest cent. The function should also validate the input values and return an error message if any of the values are invalid.
"""

def calculate_total_cost(meal_price, tax_rate, tip_percentage):
    # Check if the meal price is valid
    if meal_price <= 0:
        return "Error: Meal price must be a positive decimal value."

    # Check if the tax rate is valid
    if not (0 <= tax_rate <= 1):
        return "Error: Tax rate must be a decimal value between 0 and 1, inclusive."

    # Check if the tip percentage is valid
    if not (0 <= tip_percentage <= 1):
        return "Error: Tip percentage must be a decimal value between 0 and 1, inclusive."

    # Calculate the tax amount
    tax_amount = meal_price * tax_rate

    # Calculate the tip amount
    tip_amount = meal_price * tip_percentage

    # Calculate the total cost
    total_cost = meal_price + tax_amount + tip_amount

    # Round the total cost to the nearest cent
    rounded_total_cost = round(total_cost, 2)

    # Check if the rounded total cost exceeds the maximum representable value
    if rounded_total_cost > 9999999999.99:
        return "Error: Total cost exceeds the maximum representable value."

    # Format the total cost as a string with a dollar sign prefix
    total_cost_string = "${:.2f}".format(rounded_total_cost)

    return total_cost_string