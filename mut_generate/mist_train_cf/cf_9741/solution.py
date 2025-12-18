"""
QUESTION:
Write a function `find_cheapest_vowel_product` that takes a list of products in JSON format as input, where each product is a dictionary containing 'name' and 'cost'. The function should return the cost of the cheapest product whose name starts with a vowel (case-insensitive). If no product name starts with a vowel, the function should return None.
"""

import json

def find_cheapest_vowel_product(products):
    """
    This function finds the cost of the cheapest product from a list of products in JSON format, 
    where the product's name starts with a vowel.

    Args:
    products (list): A list of products in JSON format.

    Returns:
    float or None: The cost of the cheapest product starting with a vowel, or None if no product name starts with a vowel.
    """
    
    # Initialize variables
    cheapest_product_cost = None

    # Iterate over each product
    for product in products:
        name = product['name']
        cost = product['cost']
        
        # Check if product name starts with a vowel
        if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            # If cheapest_product_cost is None or cost is lower than the current cheapest, update the cheapest cost
            if cheapest_product_cost is None or cost < cheapest_product_cost:
                cheapest_product_cost = cost

    # Return the cost of the cheapest product
    return cheapest_product_cost