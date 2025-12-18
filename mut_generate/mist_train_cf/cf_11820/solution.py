"""
QUESTION:
Create a function `calculate_tax(price)` that takes a price as input, adds a 20% tax to the price, applies a 10% discount if the price is greater than $1000, and returns the total rounded to the nearest cent.
"""

def calculate_tax(price):
    tax_rate = 0.20
    total = price + (price * tax_rate)
    
    # Apply a discount of 10% if the price is greater than $1000
    if price > 1000:
        discount = price * 0.10
        total -= discount
    
    # Round the total to the nearest cent
    total = round(total, 2)
    
    return total