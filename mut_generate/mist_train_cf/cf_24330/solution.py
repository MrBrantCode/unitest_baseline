"""
QUESTION:
Create a function `calculate_hash` that takes a 16-bit integer as input and returns a 16-bit hash value. The input data is a hexadecimal integer, and the output hash value should also be a hexadecimal integer. The hash value for the input data 0x0010 is 0xB8C2.
"""

def calculate_hash(data):
    """
    Calculate a 16-bit hash value for the given 16-bit integer data.

    Args:
    data (int): A 16-bit integer.

    Returns:
    int: A 16-bit hash value.
    """
    # Ensure data is within 16-bit range
    data = data & 0xFFFF
    
    # Split data into two bytes
    byte1 = data >> 8
    byte2 = data & 0xFF
    
    # Calculate hash
    hash_value = (byte1 * 0x0101 + byte2 * 0x0102) & 0xFFFF
    
    return hash_value