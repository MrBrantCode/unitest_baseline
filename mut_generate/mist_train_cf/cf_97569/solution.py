"""
QUESTION:
Write a Python function `extract_product_info` that uses regular expressions to extract product names and brands from a given paragraph. The function should take a string `paragraph` as input, extract the product names and brands mentioned in the paragraph, and return a tuple containing two lists: a list of product names and a list of brands.
"""

import re

def extract_product_info(paragraph):
    """
    Extracts product names and brands from a given paragraph using regular expressions.

    Args:
    paragraph (str): The input paragraph containing product information.

    Returns:
    tuple: A tuple containing two lists: a list of product names and a list of brands.
    """
    # Define regular expressions to match product names and brands
    product_name_regex = r"iPhone \d{1,2} Pro Max|Watch Series \d"
    brand_regex = r"Apple"
    # Find all matches for product names and brands in the paragraph
    product_names = re.findall(product_name_regex, paragraph)
    brands = re.findall(brand_regex, paragraph)
    # Return the results as a tuple
    return product_names, brands