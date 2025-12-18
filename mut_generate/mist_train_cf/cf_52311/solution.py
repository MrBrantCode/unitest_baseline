"""
QUESTION:
Write a function `seven_segment_to_binary` that takes a string of 7-segment display codes as input, where each digit is represented by a specific 7-bit binary number. The function should return the binary equivalent of the input string.

Assume the following mapping from 7-segment display codes to binary numbers: 
- 0: 1111110
- 1: 0110000
- 2: 1101101
- 3: 1111001
- 4: 0110011
- 5: 1011011
- 6: 1011111
- 7: 1110000
- 8: 1111111
- 9: 1111011

Note: The input string will only contain digits from 0 to 9.
"""

def seven_segment_to_binary(s):
    """
    This function takes a string of digits as input and returns the binary equivalent of the input string.
    
    Args:
        s (str): A string of digits.
    
    Returns:
        str: The binary equivalent of the input string.
    """
    
    # Define the mapping from digits to 7-segment display codes
    segment_display_mapping = {
        '0': '1111110', '1': '0110000', '2': '1101101', '3': '1111001', '4': '0110011',
        '5': '1011011', '6': '1011111', '7': '1110000', '8': '1111111', '9': '1111011'
    }
    
    # Initialize an empty string to store the binary equivalent
    binary_equivalent = ''
    
    # Iterate over each character in the input string
    for digit in s:
        # Append the binary equivalent of the digit to the result string
        binary_equivalent += segment_display_mapping[digit]
    
    # Return the binary equivalent of the input string
    return binary_equivalent