"""
QUESTION:
Create a function called `decode_base64(encoded_s)` that takes a string `encoded_s` as input and returns its decoded Base64 representation. The function should handle errors caused by erroneous input strings by replacing or removing any characters that are not part of the Base64 character set and ensuring the input length is a multiple of four.
"""

import base64

def decode_base64(encoded_s):
    # Remove or replace characters that are not part of the Base64 character set
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    cleaned_s = ''.join(c if c in valid_chars else '_' for c in encoded_s)

    # Ensure length is a multiple of 4
    padding_needed = len(cleaned_s) % 4
    if padding_needed:
        cleaned_s += '=' * (4 - padding_needed)

    # Decode with base64
    decoded_s = base64.b64decode(cleaned_s)

    return decoded_s