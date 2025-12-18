"""
QUESTION:
Create a function called `encode_and_decode_base64` that takes a string as input, encodes it in Base64, and then decodes it back to its original form. The function should return the original string and its Base64 encoded and decoded versions.
"""

import base64

def encode_and_decode_base64(s):
    """
    Encodes a string in Base64 and then decodes it back to its original form.

    Args:
        s (str): The input string to be encoded and decoded.

    Returns:
        tuple: A tuple containing the original string, its Base64 encoded version, and its decoded version.
    """

    # Encode the string in Base64
    encoded_str = base64.b64encode(s.encode('utf-8')).decode('utf-8')

    # Decode the Base64 encoded string back to its original form
    decoded_str = base64.b64decode(encoded_str.encode('utf-8')).decode('utf-8')

    return s, encoded_str, decoded_str