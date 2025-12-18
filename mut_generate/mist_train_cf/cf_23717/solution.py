"""
QUESTION:
Design a function `shorten_url` that takes a URL as input and returns a shortened 8-character alphanumeric string. The function should map the given URL to a unique hash value and then truncate it to 8 characters.
"""

import hashlib

def shorten_url(url):
    """
    Maps the given URL to a unique hash value and then truncates it to 8 characters.
    
    Args:
    url (str): The URL to be shortened.
    
    Returns:
    str: An 8-character alphanumeric string representing the shortened URL.
    """
    
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the URL bytes
    hash_object.update(url.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    
    # Truncate the hash to 8 characters
    shortened_url = hex_dig[:8]
    
    return shortened_url