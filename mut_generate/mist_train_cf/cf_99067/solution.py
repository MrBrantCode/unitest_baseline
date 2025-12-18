"""
QUESTION:
Implement a hexadecimal encoding function `hex_encode` that takes a string input and returns the corresponding hexadecimal encoded string. Similarly, implement a hexadecimal decoding function `hex_decode` that takes a hexadecimal encoded string and returns the original string. The function should use 'utf-8' encoding scheme for conversion.
"""

def hex_encode(input_string):
    """Encodes a string into its hexadecimal equivalent using 'utf-8' encoding scheme."""
    return input_string.encode('utf-8').hex()

def hex_decode(hex_string):
    """Decodes a hexadecimal string into its original string using 'utf-8' encoding scheme."""
    return bytes.fromhex(hex_string).decode('utf-8')