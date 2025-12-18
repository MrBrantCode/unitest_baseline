"""
QUESTION:
Create a function named `generate_passphrase` that takes in a list of 5 unique words, each with a minimum of 10 characters and no repeating characters. The function should first compute the SHA-256 hash of each word, concatenate these hash values, and then use the concatenated string as the input to a PBKDF2 key derivation function with a predefined salt value and an iteration count of at least 1000. The function should return the derived passphrase as a hexadecimal string.

The salt value and iteration count can be hardcoded within the function.
"""

import hashlib
import binascii

def generate_passphrase(words):
    """
    Generate a passphrase from a list of words.

    Args:
        words (list): A list of 5 unique words, each with a minimum of 10 characters and no repeating characters.

    Returns:
        str: The derived passphrase as a hexadecimal string.
    """
    # Compute the SHA-256 hash of each word
    hashes = [hashlib.sha256(word.encode()).digest() for word in words]
    # Concatenate the hash values
    concatenated = b''.join(hashes)
    # Define the salt value
    salt = b'salt1234'
    # Derive the passphrase using PBKDF2
    passphrase = hashlib.pbkdf2_hmac('sha256', concatenated, salt, 1000)
    # Convert the passphrase to a string
    passphrase_str = binascii.hexlify(passphrase).decode()
    return passphrase_str