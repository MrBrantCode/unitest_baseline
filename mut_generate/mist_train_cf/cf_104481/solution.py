"""
QUESTION:
Create a function `calculate_total_cost` that calculates the total cost of items in a given dictionary where each item's price is stored as a tuple with four decimal places precision, and returns the total cost rounded to the nearest whole number.
"""

def calculate_total_cost(items):
    total_cost = 0.0
    for price in items.values():
        total_cost += price[0]
    return round(total_cost)