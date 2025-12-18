"""
QUESTION:
Write a function called `to_binary` that takes an integer as input and returns its binary representation as a string without leading zeros. The function must handle both positive and negative numbers, have a time complexity of O(1), and cannot use ternary expressions or built-in mathematical functions or operators.
"""

def to_binary(num):
    if num == 0:
        return '0'
    
    result = ''
    mask = 1 << 31  # Initialize mask with the leftmost bit
    
    # Loop through all 32 bits
    for i in range(32):
        # Check if the current bit is set
        if num & mask:
            result += '1'
        else:
            result += '0'
        
        # Shift the mask to the right
        mask >>= 1
    
    # Remove leading zeros
    return result.lstrip('0')