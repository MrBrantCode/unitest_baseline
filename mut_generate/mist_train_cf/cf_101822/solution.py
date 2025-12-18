"""
QUESTION:
Extract the product names and brands from a paragraph using regular expressions in Python. The product names to be extracted are in the format of "iPhone X Pro Max" or "Watch Series X", and the brand name is "Apple". Write a function `extract_products` that takes a paragraph as input and returns a tuple containing a list of product names and a list of brands.
"""

import re

def extract_products(paragraph):
    """
    Extracts product names and brands from a given paragraph.

    Args:
    paragraph (str): The input paragraph to extract product names and brands from.

    Returns:
    tuple: A tuple containing a list of product names and a list of brands.
    """
    product_name_regex = r"iPhone \d{1,2} Pro Max|Watch Series \d"
    brand_regex = r"Apple"
    product_names = re.findall(product_name_regex, paragraph)
    brands = re.findall(brand_regex, paragraph)
    return product_names, brands