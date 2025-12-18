"""
QUESTION:
Calculate the sales tax given a price and a tax rate. The function name should be `calculate_sales_tax` and it should take two parameters, `price` and `tax_rate`. The price should be a positive integer between 1 and 1000, and the tax rate should be a positive decimal number between 0.01 and 0.1. The tax rate must be rounded to the nearest hundredth decimal place before calculating the sales tax.
"""

def calculate_sales_tax(price, tax_rate):
    """
    Calculate the sales tax given a price and a tax rate.

    Args:
        price (int): The price of the item. It should be a positive integer between 1 and 1000.
        tax_rate (float): The tax rate. It should be a positive decimal number between 0.01 and 0.1.

    Returns:
        float: The sales tax amount.
    """
    sales_tax = price * round(tax_rate, 2)
    return sales_tax