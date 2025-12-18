"""
QUESTION:
Create a function `calculate_total_order_amount` that takes the quantity and price of two products, their respective discounts, and a tax rate as input, and returns the total amount of the order. The discounts and tax rate are represented as decimals. Calculate the total amount by multiplying the quantity of each product by its price and discount, then add the tax amount based on the total.
"""

def calculate_total_order_amount(quantity_productA, quantity_productB, price_productA, price_productB, discount_productA, discount_productB, tax_rate):
    total_amount = (quantity_productA * price_productA * (1 - discount_productA)) + (quantity_productB * price_productB * (1 - discount_productB))
    total_amount += total_amount * tax_rate 
    return total_amount