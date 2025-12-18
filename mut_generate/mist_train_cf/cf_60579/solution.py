"""
QUESTION:
Implement the function `limit_warning` which takes in a list of tuples (`items`) representing a sequence of additions and removals to a shopping cart, a `discount_code`, and an optional `case_sensitive` flag. The function should calculate the total cost of the items in the cart, apply the discount code if it is valid and the total exceeds the minimum cart value, and return `True` if the total exceeds the limit after applying the discount, and `False` otherwise. The `case_sensitive` flag defaults to `False`, and when set to `False`, the function should treat the discount code as case-insensitive. Assume a limit of 100 and a dictionary of predefined discount codes with their corresponding discount values and minimum cart values.
"""

from typing import List, Tuple

def limit_warning(items: List[Tuple[str, int]], discount_code: str, case_sensitive: bool = False) -> bool:
    """
    Calculate the total cost of items in a cart, apply a discount code if valid and total exceeds the minimum cart value,
    and return True if the total exceeds the limit after applying the discount, and False otherwise.

    Args:
    items (List[Tuple[str, int]]): A list of tuples representing additions and removals to a shopping cart.
    discount_code (str): A string representing a discount code.
    case_sensitive (bool): An optional flag to specify if the discount code is case-sensitive. Defaults to False.

    Returns:
    bool: True if the total exceeds the limit after applying the discount, False otherwise.
    """

    total = 0
    limit = 100

    # Query for discount codes (discount, minimum cart value)
    discount_codes = {
        'SUMMER20': (20, 100),
        'WINTER15': (15, 80),
        'AUTUMN10': (10, 70),
        'SPRING5': (5, 50)
    }

    # Calculate the total cost of items in the cart
    for action, value in items:
        if action == 'Add':
            total += value
        elif action == 'Remove':
            total -= value

    # Apply the discount code if applicable
    if discount_code in (discount_codes.keys() if case_sensitive else [key.upper() for key in discount_codes.keys()]):
        if not case_sensitive:
            discount_code = discount_code.upper()

        discount_value, min_value = discount_codes[discount_code]
        if total > min_value:
            total -= discount_value

    # Return True if the total exceeds the limit, False otherwise
    return total > limit