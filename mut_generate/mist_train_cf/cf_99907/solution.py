"""
QUESTION:
Extract the product names and brands mentioned in a paragraph using regular expressions in Python. The product names may be in the format of "iPhone X Pro Max" or "Watch Series X" where X is a single or double digit number. The brand name is "Apple". 

Implement a function `extract_product_info` that takes a string `paragraph` as input, extracts the product names and brands mentioned in the paragraph, and returns a dictionary with two keys: "product_names" and "brands", each containing a list of extracted product names and brands respectively.
"""

import re

def extract_product_info(paragraph):
    """
    Extracts product names and brands mentioned in a paragraph.
    
    Args:
        paragraph (str): The input paragraph to extract product information from.
    
    Returns:
        dict: A dictionary with two keys: "product_names" and "brands", each containing a list of extracted product names and brands respectively.
    """
    # Define regular expressions to match product names and brands
    product_name_regex = r"iPhone \d{1,2} Pro Max|Watch Series \d"
    brand_regex = r"Apple"
    
    # Find all matches for product names and brands in the paragraph
    product_names = re.findall(product_name_regex, paragraph)
    brands = re.findall(brand_regex, paragraph)
    
    # Return a dictionary with extracted product information
    return {"product_names": product_names, "brands": brands}