"""
QUESTION:
Create a function named `generate_cryptographic_identifier` that generates a distinct 32-character hexadecimal cryptographic identifier using the SHA-256 hashing algorithm. The function should take a unique identifier as input, apply the SHA-256 hashing algorithm, and then convert the hash to hexadecimal format, truncating it to 32 characters if necessary.
"""

import hashlib

def generate_cryptographic_identifier(identifier: str) -> str:
    """
    Generates a distinct 32-character hexadecimal cryptographic identifier using the SHA-256 hashing algorithm.

    Args:
    identifier (str): A unique identifier to be hashed.

    Returns:
    str: A 32-character hexadecimal cryptographic identifier.
    """
    hash_object = hashlib.sha256(identifier.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig[:32]