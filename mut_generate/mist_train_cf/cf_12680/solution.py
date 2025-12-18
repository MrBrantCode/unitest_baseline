"""
QUESTION:
Write a method named `calculate_discount` in the `DiscountCalculator` class to calculate the discount and the final price after applying the discount. The method should take no arguments other than the implicit `self` reference to the instance of the class. It should use the instance variables `price`, `cash_coupon`, and `percentage_coupon` to determine the discount and the final price. The method should return the final price after applying the discount. The method should handle cases where `price`, `cash_coupon`, or `percentage_coupon` are negative by returning the final price without applying the discount.
"""

def calculate_discount(price, cash_coupon, percentage_coupon):
    """
    Calculate the discount and the final price after applying the discount.

    Args:
        price (float): The original price.
        cash_coupon (float): The cash coupon value.
        percentage_coupon (float): The percentage coupon value.

    Returns:
        float: The final price after applying the discount.
    """

    # Initialize discount and final price
    discount = 0
    final_price = 0

    # Check if price, cash_coupon, or percentage_coupon are negative
    if price >= 0 and cash_coupon >= 0 and percentage_coupon >= 0:
        # Calculate cash coupon discount
        if price < cash_coupon:
            discount = price
        else:
            discount = cash_coupon
        
        # Calculate final price after cash coupon discount
        final_price = price - discount
        
        # Calculate percentage coupon discount
        final_price = final_price - (final_price * percentage_coupon / 100)
    
    else:
        # If any value is negative, return the original price
        final_price = price
    
    return final_price