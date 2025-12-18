"""
QUESTION:
Write a function `decode_hex_string` that takes a hexadecimal string as input and returns its decoded equivalent. The hexadecimal string is first converted to raw bytes and then decoded as a Base64 string. The function should return the decoded string in UTF-8 character encoding. The input string may contain special characters.
"""

import binascii
import base64

def decode_hex_string(s):
    raw_bytes = binascii.unhexlify(s)
    decoded_string = base64.b64decode(raw_bytes).decode('utf-8')
    return decoded_string