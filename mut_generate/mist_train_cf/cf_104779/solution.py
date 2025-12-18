"""
QUESTION:
Calculate the final price of a product after applying a discount and sales tax. Implement a function `calculate_final_price` that takes the original price and the discount rates for different customer types as input, applies a 25% discount and a 15% sales tax, and returns the final price rounded to the nearest cent.
"""

def calculate_final_price(original_price, discount_rate):
    """
    Calculate the final price of a product after applying a discount and sales tax.

    Args:
        original_price (float): The original price of the product.
        discount_rate (float): The discount rate for the customer type.

    Returns:
        float: The final price of the product after applying the discount and sales tax.
    """
    # Apply the discount
    discount_percentage = 1 - discount_rate
    discounted_price = original_price * discount_percentage
    
    # Apply the sales tax
    tax_multiplier = 1 + 0.15
    final_price = discounted_price * tax_multiplier
    
    # Round the final price to the nearest cent
    final_price = round(final_price, 2)
    
    return final_price