"""
QUESTION:
Write a function `calculate_sha256_and_size` that takes a string as input and returns the SHA-256 hash of the input string along with its size in bytes. The function should use the SHA-256 algorithm to generate the hash and calculate the size in bytes. The output should be in a human-readable format.
"""

import hashlib

def calculate_sha256_and_size(input_string):
    # Calculate the SHA-256 hash
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()

    # Calculate the size in bytes
    size_in_bytes = len(input_string.encode('utf-8'))

    return sha256_hash, size_in_bytes