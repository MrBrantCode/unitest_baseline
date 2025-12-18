"""
QUESTION:
Calculate the function `calculate_final_price(original_price, discount_rates, sales_tax_rate)` that takes the original price of a product, a list of discount rates for different customer types, and a sales tax rate as input, and returns the final price of the product after applying the highest discount and the sales tax, rounded to the nearest cent. The function should use the maximum discount rate from the provided list.
"""

def calculate_final_price(original_price, discount_rates, sales_tax_rate):
    """
    Calculate the final price of a product after applying the highest discount and sales tax.

    Args:
    original_price (float): The original price of the product.
    discount_rates (list): A list of discount rates for different customer types.
    sales_tax_rate (float): The sales tax rate.

    Returns:
    float: The final price of the product after applying the highest discount and sales tax.
    """

    # Calculate the highest discount rate
    highest_discount_rate = max(discount_rates)
    
    # Calculate the discounted price
    discounted_price = original_price - (original_price * highest_discount_rate)
    
    # Calculate the sales tax amount
    sales_tax_amount = discounted_price * sales_tax_rate
    
    # Calculate the final price
    final_price = discounted_price + sales_tax_amount
    
    # Round the final price to the nearest cent
    final_price = round(final_price, 2)
    
    return final_price