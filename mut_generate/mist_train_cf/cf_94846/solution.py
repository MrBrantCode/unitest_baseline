"""
QUESTION:
Create a function `calculate_sales_tax(price, tax_rate)` that calculates the sales tax given a price and a tax rate. The price is a positive integer between 1 and 1000, and the tax rate is a positive decimal number between 0.01 and 0.1. The tax rate should be rounded to the nearest hundredth decimal place before calculating the sales tax. The function should return the calculated sales tax amount.
"""

def calculate_sales_tax(price, tax_rate):
    sales_tax = price * round(tax_rate, 2)
    return sales_tax