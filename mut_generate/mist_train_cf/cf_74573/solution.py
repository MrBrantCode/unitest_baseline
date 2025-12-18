"""
QUESTION:
Write a function `compute_hash_value` to calculate the SHA-256 hash value of a given string. The input is a character sequence and the output should be the hash value as a hexadecimal string. Use the hashlib library in Python and ensure the input string is encoded before passing it to the hash function.
"""

import hashlib

def compute_hash_value(input_string):
    """
    Compute the SHA-256 hash value of a given string.

    Args:
        input_string (str): The input string to be hashed.

    Returns:
        str: The SHA-256 hash value as a hexadecimal string.
    """
    hash_object = hashlib.sha256(input_string.encode())
    return hash_object.hexdigest()