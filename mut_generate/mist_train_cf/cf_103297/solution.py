"""
QUESTION:
Write a function `decode_base64(encoded_s)` to decode a string `encoded_s` that was previously encoded using Base64. The function should return the decoded string in UTF-8 format.
"""

import base64

def decode_base64(encoded_s):
    decoded_s = base64.b64decode(encoded_s)
    return decoded_s.decode('utf-8')