"""
QUESTION:
Implement a function `encode_base64` that takes a string as input and returns its Base64 encoded version. The function should be able to handle strings containing non-ASCII characters.
"""

import base64

def encode_base64(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')