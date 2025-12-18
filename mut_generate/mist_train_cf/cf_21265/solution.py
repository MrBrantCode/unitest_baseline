"""
QUESTION:
Write a function named `generate_token` to create a 128-character token based on a given seed string. The token should be generated using the SHA-3 hashing algorithm and then URL encoded. The function should accept a seed string as input and return the generated token as a string. The function should use the SHA3-256 variant of the SHA-3 algorithm.
"""

import hashlib
import urllib.parse

def generate_token(seed: str) -> str:
    """
    Generates a 128-character token based on the given seed string using SHA-3 hashing and URL encoding.

    Args:
        seed (str): The seed string used to generate the token.

    Returns:
        str: The generated token.
    """
    # Hash the seed using SHA-3 (SHA3-256 in this example)
    hashed_seed = hashlib.sha3_256(seed.encode()).hexdigest()

    # Convert the hash into a 128-character hexadecimal string
    token = hashed_seed[:128]

    # Apply URL encoding to the token
    encoded_token = urllib.parse.quote(token)

    return encoded_token