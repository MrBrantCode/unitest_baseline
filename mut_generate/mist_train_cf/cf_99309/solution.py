"""
QUESTION:
Write a function named `hash_password` that takes a string password as input, hashes it using the SHA-256 algorithm with a salt, and returns the hashed password as a hexadecimal string. The salt should be 'somesalt'. The function should handle password encoding to bytes and return the hashed password as a hexadecimal string.
"""

import hashlib

def hash_password(password):
    """Hashes a password using SHA-256"""
    salt = b'somesalt'  # Add a salt to make the hash more secure
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password