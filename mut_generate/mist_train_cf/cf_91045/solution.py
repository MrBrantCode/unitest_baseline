"""
QUESTION:
Write a function `find_cheapest_vowel_product` that takes a JSON string of products as input, where each product has a 'name' and a 'cost'. The function should return the cost of the cheapest product whose name starts with a vowel (case-insensitive). If no product starts with a vowel, the function should return None. The input JSON string is in the format: '{"products": [{"name": "product_name", "cost": product_cost}, ...]}' where product_cost is a float.
"""

import json

def find_cheapest_vowel_product(json_data):
    """
    This function takes a JSON string of products as input, 
    where each product has a 'name' and a 'cost'. 
    It returns the cost of the cheapest product whose name starts with a vowel (case-insensitive). 
    If no product starts with a vowel, the function returns None.

    Args:
        json_data (str): A JSON string of products.

    Returns:
        float or None: The cost of the cheapest product starting with a vowel, or None if no product starts with a vowel.
    """

    data = json.loads(json_data)
    cheapest_product_cost = None

    for product in data['products']:
        name = product['name']
        cost = product['cost']
        
        if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            if cheapest_product_cost is None or cost < cheapest_product_cost:
                cheapest_product_cost = cost

    return cheapest_product_cost