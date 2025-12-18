"""
QUESTION:
Create a function called `decode_base64` that decodes a given Base64 encoded string with a maximum length of 1000 characters. The function should have a time complexity of O(n), where n is the length of the encoded string, and should be able to handle both upper and lower case characters. The decoded string should be returned in reverse order, preserving any special characters present in the encoded string.
"""

import base64

def decode_base64(encoded_string):
    """
    Decodes a given Base64 encoded string and returns the decoded string in reverse order.

    Args:
        encoded_string (str): The Base64 encoded string to be decoded.

    Returns:
        str: The decoded string in reverse order.
    """
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string[::-1]