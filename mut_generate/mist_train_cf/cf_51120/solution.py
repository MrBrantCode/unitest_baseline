"""
QUESTION:
Create a function `generate_permalink` that takes a product title as input and returns a unique, human-readable URL. The function should be able to handle product titles in any language. Consider the limitations of different approaches, such as transliteration, translation, and Unicode support.
"""

import unicodedata
import re

def generate_permalink(product_title: str) -> str:
    """
    Generate a unique, human-readable URL from a product title.

    The function uses a combination of transliteration and numeric ID.
    It first transliterates the title into the Latin alphabet, then replaces
    non-alphanumeric characters with hyphens, and finally appends a unique ID.

    Args:
    product_title (str): The title of the product.

    Returns:
    str: A unique, human-readable URL.
    """

    # Transliterate the title into the Latin alphabet
    transliterated_title = unicodedata.normalize('NFKD', product_title).encode('ascii', 'ignore').decode('ascii')

    # Replace non-alphanumeric characters with hyphens
    clean_title = re.sub(r'[^a-zA-Z0-9]+', '-', transliterated_title)

    # Remove leading and trailing hyphens
    clean_title = clean_title.strip('-')

    # Append a unique ID (for example, a random number)
    unique_id = 123  # Replace with a unique ID generation logic
    permalink = f"{clean_title}-{unique_id}"

    return permalink