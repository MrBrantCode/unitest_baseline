"""
QUESTION:
Create a function named `hash_password` that takes a password as input and returns its hashed value using the SHA-256 algorithm. The function should include a salt value to increase the hash's security.
"""

import hashlib

def hash_password(password):
    """Hashes a password using SHA-256"""
    salt = b'somesalt'  # Add a salt to make the hash more secure
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password