"""
QUESTION:
Write a function `verify_hash_and_size` that takes a given SHA-256 hash, its size, and an input string. The function should generate the SHA-256 hash for the input string, compare it with the provided hash, and calculate the size of the generated hash. If the generated hash matches the provided hash and the size matches the given size, the function should return "Valid hash and size". Otherwise, it should return "Invalid hash or size".
"""

import hashlib

def verify_hash_and_size(given_hash, given_size, input_string):
    """
    Verify the SHA-256 hash and size of an input string.

    Args:
    given_hash (str): The expected SHA-256 hash.
    given_size (int): The expected size of the hash.
    input_string (str): The string to generate the hash from.

    Returns:
    str: "Valid hash and size" if the generated hash matches the given hash and size, otherwise "Invalid hash or size".
    """
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    hash_size = len(sha256_hash)
    if sha256_hash == given_hash and hash_size == given_size:
        return "Valid hash and size"
    else:
        return "Invalid hash or size"