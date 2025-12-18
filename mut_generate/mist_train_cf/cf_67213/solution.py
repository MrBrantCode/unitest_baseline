"""
QUESTION:
Implement a function `extract_product_attributes` to extract product attributes from a given product title. The function should identify the brand, item, dimension, color, and model number from the product title. The function should return a dictionary with the extracted attributes. For example, given the product title "Sony ZX Series Wired On-Ear Headphones, Black MDR-ZX110", the function should return {'brand': 'Sony', 'item': 'Headphones', 'color': 'Black', 'model_number': 'MDR-ZX110'}.
"""

import re

def extract_product_attributes(product_title):
    """
    Extract product attributes from a given product title.

    Args:
    product_title (str): The title of the product.

    Returns:
    dict: A dictionary containing the extracted product attributes.
    """

    # Initialize an empty dictionary to store the product attributes
    attributes = {}

    # Use regular expression to extract the brand
    brand_match = re.match(r'^([A-Za-z]+)', product_title)
    if brand_match:
        attributes['brand'] = brand_match.group(0)

    # Use regular expression to extract the item
    item_match = re.search(r'(Headphones|Laptop|Monitor|Speaker|Camera|TV|Tablet|Phone)', product_title)
    if item_match:
        attributes['item'] = item_match.group(0)

    # Use regular expression to extract the color
    color_match = re.search(r'(Black|White|Red|Blue|Green|Yellow|Gray|Silver|Gold|Rose|Pink|Purple)', product_title)
    if color_match:
        attributes['color'] = color_match.group(0)

    # Use regular expression to extract the model number
    model_number_match = re.search(r'[A-Z]{3}-[A-Z]{2}\d{3}', product_title)
    if model_number_match:
        attributes['model_number'] = model_number_match.group(0)

    return attributes