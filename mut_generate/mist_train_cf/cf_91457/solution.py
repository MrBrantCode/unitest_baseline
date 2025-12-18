"""
QUESTION:
Create a function called `encode_string_base64` that takes a string as input and returns the Base64 encoded string. The function should be able to handle strings containing non-ASCII characters.
"""

import base64

def encode_string_base64(s):
    """
    Encodes a string using the Base64 algorithm.

    Args:
    s (str): The input string to encode.

    Returns:
    str: The Base64 encoded string.
    """
    bytes_string = s.encode('utf-8')
    base64_string = base64.b64encode(bytes_string)
    return base64_string.decode('utf-8')