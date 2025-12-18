"""
QUESTION:
Write a function named `bit_string_transformations` that takes a bit string as input and applies the following transformations: 
1. Convert every "1" to "0" and every "0" to "1".
2. Rotate the bit string to the right by 2 positions.
3. Repeat step 1.
4. Reverse the bit string.
"""

def bit_string_transformations(s):
    """
    Applies a series of transformations to a bit string.
    
    The transformations include:
    1. Inverting the bits (1 becomes 0 and 0 becomes 1)
    2. Rotating the string to the right by 2 positions
    3. Inverting the bits again
    4. Reversing the string
    
    Args:
        s (str): The input bit string.
    
    Returns:
        str: The transformed bit string.
    """
    # Invert the bits
    inverted = ''.join('1' if bit == '0' else '0' for bit in s)
    
    # Rotate the string to the right by 2 positions
    rotated = inverted[-2:] + inverted[:-2]
    
    # Invert the bits again
    inverted_again = ''.join('1' if bit == '0' else '0' for bit in rotated)
    
    # Reverse the string
    reversed_s = inverted_again[::-1]
    
    return reversed_s