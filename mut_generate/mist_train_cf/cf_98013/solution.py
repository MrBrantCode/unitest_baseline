"""
QUESTION:
Extract product names and brands from a paragraph using regular expressions in Python.

Create a function `extract_products_and_brands(paragraph)` that takes a paragraph as input and returns two lists: `product_names` and `brands`. The `product_names` list should contain product names mentioned in the paragraph (e.g., "iPhone 12 Pro Max", "Watch Series 6"), and the `brands` list should contain brand names mentioned in the paragraph (e.g., "Apple"). The function should use regular expressions to match product names and brands. Assume that product names are in the format of "iPhone <version> Pro Max" or "Watch Series <version>" and brand names are exact matches of "Apple".
"""

import re

def extract_products_and_brands(paragraph):
    """
    Extract product names and brands from a paragraph using regular expressions.

    Args:
    paragraph (str): Input paragraph containing product names and brands.

    Returns:
    tuple: Two lists, product_names and brands, containing the extracted product names and brands respectively.
    """
    # Define regular expressions to match product names and brands
    product_name_regex = r"iPhone \d{1,2} Pro Max|Watch Series \d"
    brand_regex = r"Apple"
    
    # Find all matches for product names and brands in the paragraph
    product_names = re.findall(product_name_regex, paragraph)
    brands = re.findall(brand_regex, paragraph)
    
    return product_names, brands