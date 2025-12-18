"""
QUESTION:
Write a function `hash_data` that takes a string `data` and an encryption key `key` as input. The function should hash the data using SHA-256 encryption with the provided key and return the hashed data. The function should also ensure that the hash function computations are carried out on an anonymous basis and do not store any data that could be used to link a user to a hash.
"""

import hashlib
import hmac

def hash_data(data, key):
    """
    This function hashes the input data using SHA-256 encryption with the provided key.
    
    Parameters:
    data (str): The input data to be hashed.
    key (str): The encryption key.
    
    Returns:
    str: The hashed data.
    """
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the data
    hash_object.update(data.encode('utf-8'))
    
    # Use the provided key to create an HMAC object
    hmac_object = hmac.new(key.encode('utf-8'), hash_object.digest(), hashlib.sha256)
    
    # Return the hashed data as a hexadecimal string
    return hmac_object.hexdigest()