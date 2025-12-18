"""
QUESTION:
Create a function called `calculate_discount` that takes two parameters, `membership_level` and `total_amount`, and returns the final amount to be paid after applying a discount based on the membership level. The discount percentages for different membership levels are: Silver (5%), Gold (10%), and Platinum (15%). If the membership level does not match any of these conditions, no discount should be applied.
"""

def calculate_discount(membership_level, total_amount):
    """
    Calculate the final amount to be paid after applying a discount based on the membership level.

    Args:
        membership_level (str): The level of membership (Silver, Gold, Platinum).
        total_amount (float): The total amount of the purchase.

    Returns:
        float: The final amount to be paid after applying the discount.
    """

    # Calculate discount based on membership level
    if membership_level == "Silver":
        discount = total_amount * 0.05
    elif membership_level == "Gold":
        discount = total_amount * 0.1
    elif membership_level == "Platinum":
        discount = total_amount * 0.15
    else:
        discount = 0

    # Apply discount and calculate final amount to be paid
    final_amount = total_amount - discount
    return final_amount