"""
QUESTION:
Create a function called `cryptographic_representation` that takes an input string and returns a 32-character SHA-256 hash of the string in hexadecimal format. The function should trim the hash if it exceeds 32 characters and pad it with zeros on the right if it is less than 32 characters.
"""

import hashlib

def cryptographic_representation(input_string):
    hash_object = hashlib.sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    return (hex_dig[:32] + '0' * 32)[:32]