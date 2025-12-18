"""
QUESTION:
Create a function named `calculate_total_discount` that takes three lists as parameters: `item_list`, `discount_list`, and `quantity_list`, representing the items to purchase, their corresponding discounts, and quantities, respectively. The function should calculate the total discount by multiplying the discount with the quantity for each item, considering multiple discounts for the same item based on different quantities. The function should return the total discount as a float.
"""

def calculate_total_discount(item_list, discount_list, quantity_list):
    """
    Calculate the total discount by multiplying the discount with the quantity for each item.

    Args:
        item_list (list): A list of items to purchase.
        discount_list (list): A list of discounts corresponding to each item in item_list.
        quantity_list (list): A list of quantities corresponding to each item in item_list.

    Returns:
        float: The total discount.
    """
    total_discount = 0
    
    for i in range(len(item_list)):
        total_discount += discount_list[i] * quantity_list[i]
        
    return total_discount