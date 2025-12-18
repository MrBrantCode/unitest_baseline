"""
QUESTION:
Implement a function `compress_data` that takes a list of dictionaries as input, where each dictionary represents a user with keys "user_id", "user_name", "user_age", "user_email", "user_address", and "user_phone_number". The function should compress the input data using gzip without losing any information and return the compressed data. 

The function should use the `gzip.compress` function to compress the data, and the input data should be converted to a JSON string using `json.dumps` before compression. The compressed data should be returned as a byte string.
"""

import gzip
import json

def compress_data(data):
    """
    Compress a list of dictionaries representing user data using gzip.

    Args:
    data (list): A list of dictionaries containing user information.

    Returns:
    bytes: The compressed data as a byte string.
    """
    # Convert the dataset to a JSON string
    json_str = json.dumps(data)
    
    # Compress the JSON string using gzip
    compressed_data = gzip.compress(json_str.encode())
    
    return compressed_data