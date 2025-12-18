"""
QUESTION:
Write a function `compress_strings` that compresses a list of strings into a single compressed string, and another function `decompress_string` that decompresses the compressed string back into the original list of strings, ensuring accurate decompression. The function should be space-optimized and use an efficient compression algorithm. The input and output of the functions should be as follows:
- `compress_strings`: Input - A list of strings, Output - A compressed string
- `decompress_string`: Input - A compressed string, Output - The original list of strings
"""

import zlib
import json

def compress_strings(strings):
    """Compress a list of strings into a single compressed string."""
    # Concatenate all strings in the list into a single string
    concatenated_string = json.dumps(strings)
    
    # Use zlib to compress the concatenated string
    compressed_bytes = zlib.compress(concatenated_string.encode('utf-8'))
    
    # Encode the compressed bytes to a string
    compressed_string = compressed_bytes.decode('latin1')
    
    return compressed_string


def decompress_string(compressed_string):
    """Decompress a compressed string back into the original list of strings."""
    # Decode the compressed string back to bytes
    compressed_bytes = compressed_string.encode('latin1')
    
    # Use zlib to decompress the compressed bytes
    decompressed_bytes = zlib.decompress(compressed_bytes)
    
    # Decode the decompressed bytes back to a string
    decompressed_string = decompressed_bytes.decode('utf-8')
    
    # Parse the decompressed string back into the original list of strings
    strings = json.loads(decompressed_string)
    
    return strings