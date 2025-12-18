"""
QUESTION:
Create a class with a method `decimal_to_binary(decimal_num)` that takes a non-negative integer `decimal_num` as input and returns a string of its binary representation. The method should handle the edge case where `decimal_num` is 0.
"""

def decimal_to_binary(decimal_num):
    """
    This function takes a non-negative integer as input and returns a string of its binary representation.

    Args:
        decimal_num (int): A non-negative integer.

    Returns:
        str: The binary representation of the input number as a string.
    """

    binary_string = ""
    
    # Edge case for zero
    if decimal_num == 0:
        return "0"
    
    # Convert decimal to binary
    while decimal_num > 0:
        binary_string = str(decimal_num % 2) + binary_string
        decimal_num = decimal_num // 2
    
    return binary_string