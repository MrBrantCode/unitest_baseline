"""
QUESTION:
Create a function named calculate_total_cost that takes four parameters: item_price, surcharge, discount_rate, and tax_rate. The function should return the total cost of an item, which is calculated by adding the surcharge to the item price, applying the discount rate, and then applying the tax rate. The discount rate and tax rate should be decimal values between 0 and 1.
"""

def calculate_total_cost(item_price, surcharge, discount_rate, tax_rate):
    """
    Calculate the total cost of an item, including surcharge, discount, and tax.

    Args:
        item_price (float): The original price of the item.
        surcharge (float): Any additional charges applied to the item price.
        discount_rate (float): The percentage discount applied to the item price, between 0 and 1.
        tax_rate (float): The percentage tax rate applied to the total cost of the item, including any surcharges or discounts.

    Returns:
        float: The total cost of the item, including surcharge, discount, and tax.
    """
    return (item_price + surcharge) * (1 - discount_rate) * (1 + tax_rate)