"""
QUESTION:
Create a function `generate_passphrase(words, salt, iterations)` that takes in a list of five unique words, a salt value, and an iteration count, and returns a passphrase. The function should first compute the SHA-256 hash of each word, concatenate these hashes, and then use the PBKDF2 key derivation function with the given salt and iteration count to derive the passphrase. The output passphrase should be a string. The iteration count should be at least 1000.
"""

import hashlib
import binascii

def generate_passphrase(words, salt, iterations):
    """
    Generate a passphrase from a list of words, salt, and iteration count.

    Args:
        words (list): A list of unique words.
        salt (bytes): The salt value.
        iterations (int): The iteration count.

    Returns:
        str: The generated passphrase.
    """
    # Compute the SHA-256 hash of each word
    hashes = [hashlib.sha256(word.encode()).digest() for word in words]
    # Concatenate the hash values
    concatenated = b''.join(hashes)
    # Derive the passphrase using PBKDF2
    passphrase = hashlib.pbkdf2_hmac('sha256', concatenated, salt, iterations)
    # Convert the passphrase to a string
    passphrase_str = binascii.hexlify(passphrase).decode()
    return passphrase_str