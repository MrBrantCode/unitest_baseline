"""
QUESTION:
Write a function called `hash_password` that takes a password as input, hashes it using the SHA-256 algorithm, and returns the hashed password. The function should also add a salt to the password before hashing it.
"""

import hashlib

def hash_password(password):
    """Hashes a password using SHA-256"""
    salt = b'somesalt'  # Add a salt to make the hash more secure
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password