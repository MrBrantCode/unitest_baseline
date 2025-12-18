"""
QUESTION:
Create a function called `calculate_total_discount` that takes three lists as input: a list of items, a list of corresponding discounts, and a list of corresponding quantities. The function should calculate the total discount by multiplying each item's discount by its quantity, summing these values, and returning the total discount. The lists are assumed to be of equal length.
"""

def calculate_total_discount(item_list, discount_list, quantity_list):
    """
    Calculate the total discount by multiplying each item's discount by its quantity.

    Args:
    item_list (list): A list of items.
    discount_list (list): A list of corresponding discounts.
    quantity_list (list): A list of corresponding quantities.

    Returns:
    float: The total discount.
    """
    return sum(discount * quantity for discount, quantity in zip(discount_list, quantity_list))