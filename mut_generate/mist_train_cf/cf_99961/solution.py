"""
QUESTION:
Implement a function called `generate_passphrase` that takes a list of 5 words and returns a passphrase. The function should compute the SHA-256 hash of each word, concatenate the hash values, and then use the concatenated string as input to a PBKDF2 key derivation function with a salt value and an iteration count of at least 1000. The output of the PBKDF2 function should be the passphrase. The function should return the passphrase as a hexadecimal string.
"""

import hashlib
import binascii

def generate_passphrase(words):
    """
    Generates a passphrase from a list of 5 words.

    Args:
    words (list): A list of 5 words.

    Returns:
    str: The generated passphrase as a hexadecimal string.
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