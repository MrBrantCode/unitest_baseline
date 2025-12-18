"""
QUESTION:
Create a function `extract_prices` that takes an HTML string as input and returns a list of prices mentioned in the string. The function should be able to handle different currency symbols (£, €, $), decimal separators (., or ,), and thousand separators (,). It should also handle variations in price formats, such as "1.45 GBP" instead of "£1.45", and prices mentioned multiple times for the same item.
"""

import re

def extract_prices(html_string):
    """
    Extracts prices from an HTML string.

    This function takes an HTML string as input and returns a list of prices mentioned in the string.
    It handles different currency symbols (£, €, $), decimal separators (., or ,), and thousand separators (,).
    It also handles variations in price formats, such as "1.45 GBP" instead of "£1.45", and prices mentioned multiple times for the same item.

    Parameters:
    html_string (str): The HTML string to extract prices from.

    Returns:
    list: A list of prices mentioned in the HTML string.
    """
    # Parse the HTML string to identify all div tags, including nested div tags
    div_tags = re.findall(r"<div.*?</div>", html_string, re.DOTALL)

    # Extract the text content of each div tag
    div_texts = [re.sub(r"<.*?>", "", div_tag) for div_tag in div_tags]

    # Extract the prices from the extracted text
    price_pattern = r"(?:[£€$]\s?)?(\d+(?:[,.]\d{3})*(?:[,.]\d{1,2})?)\s?(?:GBP|USD|EUR)?"
    prices = [re.findall(price_pattern, div_text) for div_text in div_texts]

    # Flatten the list of lists into a single list
    prices = [price for sublist in prices for price in sublist]

    return prices