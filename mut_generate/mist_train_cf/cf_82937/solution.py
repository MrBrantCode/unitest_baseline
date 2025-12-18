"""
QUESTION:
Create a function named `create_key` that takes a password as input and returns a 256-bit encryption key using the SHA256 hashing algorithm. The function should not take any other parameters and should return a hash digest.
"""

import hashlib

def create_key(password):
    """
    This function generates a 256-bit encryption key using the SHA256 hashing algorithm.

    Args:
        password (str): The password to be used for key generation.

    Returns:
        bytes: A 256-bit hash digest.
    """
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.digest()