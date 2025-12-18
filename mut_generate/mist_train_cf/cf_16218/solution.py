"""
QUESTION:
Write a function `find_cheapest_product` that finds the cost of the cheapest product from a given list of products in JSON format. The product's name must start with a vowel and be in stock. The function should return the cost of the cheapest product if found, otherwise, it should return a message indicating that no product was found. The JSON data should be in the format of a list of objects, with each object representing a product and having properties "name", "cost", "stock", and "description".
"""

import json

def find_cheapest_product(json_data):
    """
    Finds the cost of the cheapest product from a given list of products in JSON format.
    
    The product's name must start with a vowel and be in stock.
    
    Args:
        json_data (str): A JSON string containing the list of products.
        
    Returns:
        float or str: The cost of the cheapest product if found, otherwise a message indicating that no product was found.
    """

    # Read the JSON data containing the list of products
    products = json.loads(json_data)

    # Initialize variables
    cheapest_cost = float('inf')
    cheapest_product = None

    # Iterate through each product
    for product in products:
        # Check if the product is in stock
        if product['stock'] == 'in stock':
            # Check if the name starts with a vowel
            if product['name'][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                # Check if the cost is lower than cheapest_cost
                if product['cost'] < cheapest_cost:
                    cheapest_cost = product['cost']
                    cheapest_product = product

    # Check if there is a cheapest product found
    if cheapest_product is None:
        return "No cheapest product found."
    else:
        # Return the cost of the cheapest product
        return cheapest_product['cost']