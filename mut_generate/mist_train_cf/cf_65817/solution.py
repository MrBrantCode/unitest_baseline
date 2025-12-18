"""
QUESTION:
Create a program that can perform the following operations on Base64 encoded strings:
- Decode the string into a human-readable format considering special characters.
- Compare two decoded strings for equality.
- Check if a decoded string contains a certain sequence of characters.

Develop functions for these operations with the following names: 
- `decode_string(encoded_string)`: takes a Base64 encoded string as input and returns the decoded string.
- `compare_strings(decoded_string_1, decoded_string_2)`: takes two decoded strings as input and returns a boolean indicating whether they are equal.
- `contains_sequence(decoded_string, sequence)`: takes a decoded string and a sequence of characters as input and returns a boolean indicating whether the sequence exists in the string.
"""

import base64

def decode_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string).decode()
    return decoded_string

def compare_strings(decoded_string_1, decoded_string_2):
    return decoded_string_1 == decoded_string_2

def contains_sequence(decoded_string, sequence):
    return sequence in decoded_string