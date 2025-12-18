"""
QUESTION:
Create a function called `hash_password` that takes a password as input and returns its hashed version. The function should use the SHA-256 hashing algorithm and include a salt for added security. The input password is a string and the output should be a hexadecimal string.
"""

import hashlib

def hash_password(password):
    """Hashes a password using SHA-256"""
    salt = b'somesalt'  # Add a salt to make the hash more secure
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password