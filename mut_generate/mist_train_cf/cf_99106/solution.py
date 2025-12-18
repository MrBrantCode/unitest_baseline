"""
QUESTION:
Write a function `generate_key` that takes in a list of salts, a list of passwords, a key length (default is 32), and an iteration count (default is 100,000) as input. The function should return a key generated using the `pbkdf2_hmac` function with the SHA-256 digest algorithm. The function should concatenate all salts and passwords before passing them through the `pbkdf2_hmac` function to maintain the same level of security.
"""

import hashlib

def generate_key(salts, passwords, key_length=32, iterations=100000):
    concatenated_salt = b''
    for salt in salts:
        concatenated_salt += salt.encode()
    concatenated_password = b''
    for password in passwords:
        concatenated_password += password.encode()
    key = hashlib.pbkdf2_hmac('sha256', concatenated_password, concatenated_salt, iterations, dklen=key_length)
    return key