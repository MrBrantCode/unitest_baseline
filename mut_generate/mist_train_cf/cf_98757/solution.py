"""
QUESTION:
Implement a function named `represent_product_info` that uses the JSON format to structure and display product information in a user-friendly manner. The function should take in a dictionary representing product information, with the following keys: `name`, `description`, `price`, and `specs`. The `specs` key should map to another dictionary containing product specifications. The function should return a JSON-formatted string representing the product information.
"""

import json

def represent_product_info(product_info):
    """
    Returns a JSON-formatted string representing the product information.

    Args:
        product_info (dict): A dictionary containing product information with keys 'name', 'description', 'price', and 'specs'.

    Returns:
        str: A JSON-formatted string representing the product information.
    """
    return json.dumps(product_info, indent=4)