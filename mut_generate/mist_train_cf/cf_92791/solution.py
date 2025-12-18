"""
QUESTION:
Create a function called `reverse_base64_encode` that takes a string as input and returns a base64 encoded version of the string in reverse order. The function should use the standard base64 alphabet and padding characters, but the encoded string should be reversed after encoding.
"""

import base64

def reverse_base64_encode(text):
    encoded = base64.b64encode(text.encode()).decode()
    reversed_encoded = encoded[::-1]
    return reversed_encoded