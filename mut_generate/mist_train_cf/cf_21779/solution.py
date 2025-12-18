"""
QUESTION:
Extract all prices of items from a given HTML string using regular expressions, considering different currency symbols (£, €, $), formats, decimal separators (., ,), and thousand separators (,). The function should handle cases where prices are mentioned multiple times, in different currencies, or with variations in formatting.

The function `extract_prices(html_string)` takes an HTML string as input and returns a list of extracted prices. The HTML string may contain nested div tags and prices may be mentioned in different formats.
"""

import re

def extract_prices(html_string):
    """
    Extracts prices from an HTML string.

    Args:
        html_string (str): The input HTML string.

    Returns:
        list: A list of extracted prices.
    """
    # Extract all div tags from the HTML string
    div_tags = re.findall(r"<div.*?</div>", html_string, re.DOTALL)

    # Extract text content from each div tag
    div_texts = [re.sub(r"<.*?>", "", div_tag) for div_tag in div_tags]

    # Define the price pattern
    price_pattern = r"(?:[£€$]\s?)?(\d+(?:[,.]\d{3})*(?:[,.]\d{1,2})?)\s?(?:GBP|USD|EUR)?"

    # Extract prices from the text content
    prices = [price for div_text in div_texts for price in re.findall(price_pattern, div_text)]

    return prices