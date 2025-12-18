"""
QUESTION:
Write a function `decode_base64` that takes a Base64 encoded string as input, decodes it, and returns the decoded string in reverse order. The function should have a time complexity of O(n), where n is the length of the encoded string, and be able to handle strings with a maximum length of 1000 characters.
"""

import base64

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode("utf-8")
    return decoded_string[::-1]