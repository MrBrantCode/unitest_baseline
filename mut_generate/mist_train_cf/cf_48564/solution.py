"""
QUESTION:
Write a function named `decodeslug` that takes a URL slug as input. The function should first decode any URL-encoded characters in the slug, replacing hyphens with spaces. If the resulting string is a valid Base64-encoded string, the function should then decode it into its original string format using UTF-8 encoding. If the string is not a valid Base64-encoded string, the function should return the URL-decoded string as is.
"""

import base64
from urllib.parse import unquote

def decodeslug(slug):
    # Decoding slug text to normal
    decoded_slug = unquote(slug).replace("-", " ")

    # Checking and decoding base64
    try:
        decoded_str_byte = base64.b64decode(decoded_slug + "===") 
        decoded_str = decoded_str_byte.decode("utf-8")
        return decoded_str
    except: 
        return decoded_slug