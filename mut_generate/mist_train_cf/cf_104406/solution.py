"""
QUESTION:
Write a function named "xor_and_shift" that takes two unsigned 8-bit integers and a mask value as input, performs a bitwise XOR operation, applies a bitwise AND operation with the mask value, and then performs a left shift operation by 4 bits on the result. The mask value is 0xFF.
"""

def xor_and_shift(data1, data2):
    """
    This function takes two unsigned 8-bit integers, performs a bitwise XOR operation, 
    applies a bitwise AND operation with a mask value (0xFF), and then performs a left 
    shift operation by 4 bits on the result.

    Args:
        data1 (int): The first unsigned 8-bit integer.
        data2 (int): The second unsigned 8-bit integer.

    Returns:
        int: The result of the operations.
    """

    # Perform a bitwise XOR operation on data1 and data2
    xor_result = data1 ^ data2
    
    # Apply a bitwise AND operation with the mask value (0xFF)
    and_result = xor_result & 0xFF
    
    # Perform a left shift operation by 4 bits on the result
    shift_result = and_result << 4
    
    return shift_result