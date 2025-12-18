"""
QUESTION:
Calculate the final selling price of an item after two successive discounts. The function `calculate_final_selling_price` should take the original price and two discount percentages as input, and return the final selling price.
"""

def calculate_final_selling_price(original_price, first_discount_percent, second_discount_percent):
    """
    Calculate the final selling price of an item after two successive discounts.

    Args:
        original_price (float): The original price of the item.
        first_discount_percent (float): The first discount percentage.
        second_discount_percent (float): The second discount percentage.

    Returns:
        float: The final selling price.
    """
    # Calculate the first discount
    first_discount = original_price * first_discount_percent / 100
    
    # Calculate the price after the first discount
    after_first_discount = original_price - first_discount
    
    # Calculate the second discount
    second_discount = after_first_discount * second_discount_percent / 100
    
    # Calculate the final selling price
    final_selling_price = after_first_discount - second_discount
    
    return final_selling_price