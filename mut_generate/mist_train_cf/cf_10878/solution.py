"""
QUESTION:
Create a function `calculate_sales_tax(price, tax_rate)` that takes two parameters: `price`, a positive integer between 1 and 1000, and `tax_rate`, a positive decimal number between 0.01 and 0.1. The function should return the sales tax calculated by multiplying the `price` by the `tax_rate`, rounded to the nearest hundredth decimal place.
"""

def calculate_sales_tax(price, tax_rate):
    sales_tax = round(price * tax_rate, 2)
    return sales_tax