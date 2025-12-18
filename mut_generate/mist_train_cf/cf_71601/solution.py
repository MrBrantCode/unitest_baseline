"""
QUESTION:
Write a function named `calculate_total_cost` that takes three parameters: a list of dictionaries representing items in a shopping cart (`cart`), a shipping cost (`shipping_cost`), and a tax rate (`tax_rate`). Each dictionary in the cart should have the keys 'name', 'price', and 'quantity'. The function should return the total cost of the shopping cart after adding the shipping cost and tax, rounded to two decimal places.
"""

def calculate_total_cost(cart, shipping_cost, tax_rate):
    # Calculate the subtotal
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    
    # Add shipping cost
    total_cost = subtotal + shipping_cost
    
    # Add taxes
    total_cost += total_cost * tax_rate
    
    return round(total_cost, 2)