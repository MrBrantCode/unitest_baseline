"""
QUESTION:
Write a function `calculate_sales_tax` that takes two parameters: `price` and `tax_rate`. The function should calculate the sales tax amount by multiplying the `price` with the `tax_rate` rounded to the nearest hundredth decimal place. The `price` should be a positive integer between 1 and 1000, and the `tax_rate` should be a positive decimal number between 0.01 and 0.1.
"""

def calculate_sales_tax(price, tax_rate):
    rounded_tax_rate = round(tax_rate, 2)
    sales_tax = price * rounded_tax_rate
    return sales_tax