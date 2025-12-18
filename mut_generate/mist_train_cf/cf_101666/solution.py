"""
QUESTION:
Create a function `generate_passphrase` that generates a passphrase by taking a list of five unique words as input, each with at least 10 characters, and returns the derived passphrase. The function should use the SHA-256 algorithm to hash each word, concatenate these hash values, and then use the PBKDF2 key derivation function with a salt value and at least 1000 iterations to derive the passphrase.
"""

import hashlib
import binascii
import os

def generate_passphrase(words):
    """
    Generate a passphrase by taking a list of five unique words as input, 
    each with at least 10 characters, and return the derived passphrase.

    The function uses the SHA-256 algorithm to hash each word, 
    concatenate these hash values, and then use the PBKDF2 key derivation 
    function with a salt value and at least 1000 iterations to derive the passphrase.

    Args:
        words (list): A list of five unique words, each with at least 10 characters.

    Returns:
        str: The derived passphrase.
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