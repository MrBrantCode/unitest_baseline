"""
QUESTION:
Create a function named `calculate_total_order_amount` that takes in the quantity, price, and discount of two products, and a tax rate. Calculate and return the total amount of the order, where each product's price is discounted by the given percentage, and then the total is increased by the given tax rate (also a percentage). All percentages should be represented as decimals in the function parameters.
"""

def calculate_total_order_amount(quantity_productA, quantity_productB, price_productA, price_productB, discount_productA, discount_productB, tax_rate):
    total_amount = (quantity_productA * price_productA * (1 - discount_productA)) + (quantity_productB * price_productB * (1 - discount_productB))
    total_amount += total_amount * tax_rate 
    return total_amount