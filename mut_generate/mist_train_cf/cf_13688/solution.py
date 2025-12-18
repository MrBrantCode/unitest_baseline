"""
QUESTION:
Calculate the function `calculate_final_price` that takes two parameters: `original_price`, `discount_rate`, and `tax_rate` representing the original price of a product, the discount rate as a decimal, and the sales tax rate as a decimal, respectively, and returns the final price of the product after applying the discount and then the sales tax. The function should accept any valid non-negative numbers as input for the original price and rates between 0 and 1 for the discount and tax rates.
"""

def calculate_final_price(original_price, discount_rate, tax_rate):
    """
    Calculate the final price of a product after applying a discount and then sales tax.

    Args:
        original_price (float): The original price of the product.
        discount_rate (float): The discount rate as a decimal.
        tax_rate (float): The sales tax rate as a decimal.

    Returns:
        float: The final price of the product.
    """
    # Calculate the discount amount
    discount_amount = original_price * discount_rate
    
    # Calculate the discounted price
    discounted_price = original_price - discount_amount
    
    # Calculate the tax amount
    tax_amount = discounted_price * tax_rate
    
    # Calculate the final price
    final_price = discounted_price + tax_amount
    
    return final_price