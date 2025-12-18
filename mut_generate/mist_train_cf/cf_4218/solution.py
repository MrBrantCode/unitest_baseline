"""
QUESTION:
Create a function named `calculate_tax` that takes one argument `price` and returns the total price after applying a 20% tax, a 10% discount if the price is over $1000, a 5% surcharge if the total price is between $500 and $1000, a $50 service fee if the total price is less than $100, and a 2% handling fee if the total price is over $2000. The total price should be rounded to the nearest cent.
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
    
    # Add a surcharge of 5% if the total is greater than $500 and less than $1000
    if total > 500 and total < 1000:
        surcharge = total * 0.05
        total += surcharge
    
    # Add a service fee of $50 if the total is less than $100
    if total < 100:
        total += 50
    
    # Increase the difficulty by adding a handling fee of 2% if the total is greater than $2000
    if total > 2000:
        handling_fee = total * 0.02
        total += handling_fee
    
    return total