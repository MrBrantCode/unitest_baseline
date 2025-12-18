"""
QUESTION:
Write a function `compress_and_decompress_dataset` that takes a list of user dictionaries as input and returns the decompressed data after compressing it using gzip compression algorithm. The function should handle the compression and decompression of the data. The input dataset is a list of dictionaries, where each dictionary contains information about a user, including 'user_id', 'user_name', 'user_age', 'user_email', 'user_address', and 'user_phone_number'. The function should not take any additional parameters.
"""

import gzip
import json

def compress_and_decompress_dataset(dataset):
    """
    This function takes a list of user dictionaries, compresses it using gzip, 
    decompresses it, and returns the decompressed data.
    
    Args:
        dataset (list): A list of dictionaries containing user information.
        
    Returns:
        list: The decompressed list of dictionaries.
    """
    
    # Convert the dataset to a JSON string
    json_str = json.dumps(dataset)
    
    # Compress the JSON string using gzip
    compressed_data = gzip.compress(json_str.encode())
    
    # Decompress the data using gzip
    decompressed_data = gzip.decompress(compressed_data)
    
    # Convert the decompressed data back to a list of dictionaries
    dataset = json.loads(decompressed_data.decode())
    
    return dataset