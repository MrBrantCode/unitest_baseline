"""
QUESTION:
Write a function named `encode_text` that takes a string input, encodes it into base64, and returns the encoded string. The input string should be encoded into bytes using UTF-8 encoding before base64 encoding, and the resulting bytes should be decoded back into a string using UTF-8 encoding.
"""

import base64

def encode_text(input_text):
    ulysses = input_text.encode('utf-8')
    base64_bytes = base64.b64encode(ulysses)
    base64_text = base64_bytes.decode('utf-8')
    return base64_text