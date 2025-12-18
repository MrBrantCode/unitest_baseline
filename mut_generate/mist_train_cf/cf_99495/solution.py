"""
QUESTION:
Create a function named `generate_passphrase` that takes a list of unique words, each with at least 10 characters, as input. The function should convert each word into a hash value using the SHA-256 algorithm, concatenate these hash values together, and then use the result as the input of a PBKDF2 key derivation function with a salt value and an iteration count of at least 1000. The function should return the derived passphrase as a string.
"""

import hashlib
import binascii

def generate_passphrase(words, salt, iterations=1000):
    """
    Generate a passphrase from a list of words using SHA-256 and PBKDF2.

    Args:
    words (list): A list of unique words, each with at least 10 characters.
    salt (bytes): A salt value for the PBKDF2 key derivation function.
    iterations (int, optional): The number of iterations for the PBKDF2 key derivation function. Defaults to 1000.

    Returns:
    str: The derived passphrase as a string.
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