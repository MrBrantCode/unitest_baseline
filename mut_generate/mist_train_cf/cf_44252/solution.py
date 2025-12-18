"""
QUESTION:
Create a function `encode_str(s)` that encodes an alphanumeric string `s` using a custom base-64 algorithm and another function `decode_str(s)` that decodes the encoded string back to its original form. The functions should handle alphanumeric strings of up to 50 characters in length.
"""

import base64

def encode_str(s):
    b = bytearray(s, 'utf-8')
    b64 = base64.b64encode(b)
    return str(b64, 'utf-8')

def decode_str(s):
    b64 = bytearray(s, 'utf-8')
    b = base64.b64decode(b64)
    return str(b, 'utf-8')