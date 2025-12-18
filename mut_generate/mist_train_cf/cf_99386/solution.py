"""
QUESTION:
Extract product names and brands from a given paragraph using regular expressions in Python. Define a function named `extract_product_info` that takes a paragraph as input and returns two lists: product names and brands. The function should use the `re` module to match product names and brands in the paragraph. The product names are in the format "iPhone X Pro Max" or "Watch Series X" where X is a single or double-digit number, and the brand name is "Apple".
"""

import re

def extract_product_info(paragraph):
    # Define regular expressions to match product names and brands
    product_name_regex = r"iPhone \d{1,2} Pro Max|Watch Series \d"
    brand_regex = r"Apple"
    # Find all matches for product names and brands in the paragraph
    product_names = re.findall(product_name_regex, paragraph)
    brands = re.findall(brand_regex, paragraph)
    # Return the results
    return product_names, brands