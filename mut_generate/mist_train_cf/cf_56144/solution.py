"""
QUESTION:
Design a function named `decode` to decode a given string encrypted with Base64 encryption. The function should correct any inherent padding errors by appending "=" to underpadded strings. If other errors occur during decoding, the function should catch the exception and return an error message. The decoded string should be returned as a UTF-8 encoded string.
"""

import base64

def decode(encoded_str):
    padding = 4 - (len(encoded_str) % 4)
    if padding < 4:
        encoded_str += "=" * padding  # correct padding if necessary
    try:
        return base64.b64decode(encoded_str).decode('utf-8')
    except Exception as e:
        return 'Error: ' + str(e)