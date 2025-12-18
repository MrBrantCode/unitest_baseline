"""
QUESTION:
Create a function `calculate_juice_price` that calculates the cost per glass of juice and the price per glass to maintain a certain profit margin after adding an exotic fruit. The function should take in the following parameters: `current_cost`, `profit_margin`, `exotic_fruit_cost`, `exotic_fruit_per_glass`, `shipping_cost_per_pound`, and `glasses_per_pound`. The function should return the new cost per glass and the price per glass to maintain the current profit margin. Assume all input values are in dollars except for `glasses_per_pound` which is in glasses per pound, and `profit_margin` which is a decimal value representing the percentage.
"""

def calculate_juice_price(current_cost, profit_margin, exotic_fruit_cost, exotic_fruit_per_glass, shipping_cost_per_pound, glasses_per_pound):
    """
    Calculate the cost per glass of juice and the price per glass to maintain a certain profit margin after adding an exotic fruit.

    Args:
    current_cost (float): The current cost per glass of juice in dollars.
    profit_margin (float): The desired profit margin as a decimal value.
    exotic_fruit_cost (float): The cost of exotic fruit per pound in dollars.
    exotic_fruit_per_glass (float): The amount of exotic fruit needed per glass of juice in pounds.
    shipping_cost_per_pound (float): The shipping cost per pound of exotic fruit in dollars.
    glasses_per_pound (float): The number of glasses of juice per pound of fruit.

    Returns:
    tuple: A tuple containing the new cost per glass and the price per glass to maintain the current profit margin.
    """
    exotic_fruit_cost_per_glass = (exotic_fruit_cost + shipping_cost_per_pound) * exotic_fruit_per_glass / glasses_per_pound
    new_cost_per_glass = current_cost + exotic_fruit_cost_per_glass
    price_per_glass = new_cost_per_glass / (1 - profit_margin)
    return new_cost_per_glass, price_per_glass