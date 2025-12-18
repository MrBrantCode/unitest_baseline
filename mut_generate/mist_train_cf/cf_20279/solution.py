"""
QUESTION:
Create a method called "calculate_total_price" that takes an additional parameter "tax_percentage" and returns the final price of an item after applying a discount and adding tax. The method should use the instance variables "price", "cash_coupon", and "percentage_coupon" to calculate the discount. If the price is lower than the cash coupon, the discount should be equal to the price; otherwise, it should be equal to the cash coupon. The method should also subtract the percentage coupon discount from the price after the cash coupon discount, and then add the tax to the final price. The method should only calculate the final price if all the input values (price, cash_coupon, percentage_coupon, and tax_percentage) are non-negative.
"""

def calculate_total_price(price, cash_coupon, percentage_coupon, tax_percentage):
    """
    Calculate the final price of an item after applying a discount and adding tax.

    Args:
        price (float): The initial price of the item.
        cash_coupon (float): The cash coupon amount.
        percentage_coupon (float): The percentage coupon amount.
        tax_percentage (float): The tax percentage.

    Returns:
        float: The final price after applying the discount and adding the tax.
    """

    if price < 0 or cash_coupon < 0 or percentage_coupon < 0 or tax_percentage < 0:
        return 0

    # Calculate the discount
    discount = min(price, cash_coupon)

    # Calculate the price after the cash coupon discount
    price_after_cash_discount = price - discount

    # Calculate the price after the percentage coupon discount
    price_after_percentage_discount = price_after_cash_discount - (price_after_cash_discount * percentage_coupon / 100)

    # Calculate the final price by adding the tax
    final_price = price_after_percentage_discount + (price_after_percentage_discount * tax_percentage / 100)

    return final_price