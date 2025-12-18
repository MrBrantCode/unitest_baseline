"""
QUESTION:
Create a function named `perform_hash` that takes a string input and returns a tuple of hashed strings. The function should perform a SHA256 hash operation on the input string and return the hexadecimal representation of the digest if the input string contains only alphanumeric characters. If the input string is not alphanumeric, the function should return an error message.
"""

import hashlib

def perform_hash(input_str):
    """
    This function performs a SHA256 hash operation on the input string and returns 
    the hexadecimal representation of the digest if the input string contains only 
    alphanumeric characters. If the input string is not alphanumeric, the function 
    returns an error message.

    Parameters:
    input_str (str): The input string to be hashed.

    Returns:
    str: A tuple containing the hashed string if the input is alphanumeric, 
    otherwise an error message.
    """
    if isinstance(input_str, str) and input_str.isalnum(): 
        hash_obj = hashlib.sha256(input_str.encode())
        return (hash_obj.hexdigest(),)
    else:
        return (f'Invalid input: {input_str}',)