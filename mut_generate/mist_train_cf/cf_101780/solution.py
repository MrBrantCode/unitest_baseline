"""
QUESTION:
Create a function named `hash_password(password)` that takes a password as input and returns its hashed value using the SHA-256 algorithm with a salt. The function should encode the password to bytes before hashing and append the salt to the password before hashing. The salt should be a bytes object. The function should return the hashed password as a hexadecimal string.
"""

import hashlib

def hash_password(password):
    """
    Hashes a password using SHA-256.
    
    Args:
        password (str): The password to be hashed.
    
    Returns:
        str: The hashed password as a hexadecimal string.
    """
    salt = b'somesalt'  # Add a salt to make the hash more secure
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password