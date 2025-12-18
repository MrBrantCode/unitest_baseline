"""
QUESTION:
Create a function named `crypto_embodiment` that takes an input string, generates a SHA-256 hash of the string, encodes it in hexadecimal, and returns the first 32 characters of the encoded hash. The function should be implemented in Python and the resulting hash should be 32 characters long.
"""

import hashlib

def crypto_embodiment(input_string):
    sha_signature = hashlib.sha256(input_string.encode()).hexdigest()
    return sha_signature[:32]