"""
QUESTION:
Write a function `reverse_base64_encode(text)` that takes a string `text` as input, encodes it into base64, reverses the encoded string, and returns the result. The input string should be encoded into base64 in the usual manner, but the resulting encoded string should be reversed. The function should not have any restrictions on the length of the input string.
"""

import base64

def reverse_base64_encode(text):
    encoded = base64.b64encode(text.encode()).decode()
    reversed_encoded = encoded[::-1]
    return reversed_encoded