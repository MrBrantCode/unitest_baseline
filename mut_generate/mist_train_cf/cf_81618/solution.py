"""
QUESTION:
Implement the concept of "calculate_total" in Python, where the function calculates the total cost of items. The function should be able to handle two different scenarios: 
- taking a single argument for a single item's price and a default quantity of 1, and 
- taking two arguments for the item's price and quantity.
"""

def calculate_total(price, quantity=1):
    return price * quantity