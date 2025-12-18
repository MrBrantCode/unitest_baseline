"""
QUESTION:
Implement a function `calculate_revenue` that calculates the total revenue given the number of units and the price per unit. The function should be able to handle both integer and float inputs for `num_units` and `price_per_unit`.
"""

def calculate_revenue(num_units, price_per_unit):
    revenue = num_units * price_per_unit
    return revenue