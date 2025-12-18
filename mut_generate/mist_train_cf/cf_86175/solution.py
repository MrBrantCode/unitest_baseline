"""
QUESTION:
Write a function `clean_url_generator` that takes in a `product_name` and `product_id` and generates a clean URL in the format `site.com/product/product_name/`. Assume that you are using a cache to store the mapping between product names and IDs, and that product names are unique. What are the potential risks/issues with this approach, and how would you address conflicts when two products have the same name? 

Restrictions: Consider performance issues, URL encoding, and special characters in the product name.
"""

import urllib.parse

def clean_url_generator(product_name, product_id):
    """
    Generates a clean URL in the format site.com/product/product_name/

    Args:
        product_name (str): The name of the product.
        product_id (int): The ID of the product.

    Returns:
        str: A clean URL.
    """
    # URL encode the product name to handle special characters
    encoded_product_name = urllib.parse.quote_plus(product_name)
    
    # Generate the clean URL
    clean_url = f"site.com/product/{encoded_product_name}/"
    
    return clean_url