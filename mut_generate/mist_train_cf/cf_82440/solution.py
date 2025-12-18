"""
QUESTION:
Create a function called `unique_alphanumeric_chars` that takes a string as input and returns the count and unique alphanumeric characters in ascending ASCII value. The function should consider case sensitivity and exclude non-alphanumeric characters.
"""

def unique_alphanumeric_chars(paragraph):
    """
    Returns the count and unique alphanumeric characters in ascending ASCII value.

    Args:
        paragraph (str): Input string.

    Returns:
        tuple: A tuple containing the count and a string of unique alphanumeric characters in ascending ASCII value.
    """
    unique_chars = sorted(set(ch for ch in paragraph if ch.isalnum()))
    count = len(unique_chars)
    return count, ''.join(unique_chars)