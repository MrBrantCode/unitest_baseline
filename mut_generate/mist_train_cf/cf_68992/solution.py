"""
QUESTION:
Write a function named `octal_gray` that takes an octal number as a string input, converts it into its equivalent binary representation, and then into gray code, while maintaining the sign magnitude notation. The function should handle both positive and negative inputs, keeping the sign separate without applying the Gray code conversion. The output should be a string representing the gray code equivalent of the input octal number, without the '0b' prefix.
"""

def octal_gray(octal):
    # Check for negative input and store the sign
    sign = ''
    if octal[0] == '-':
        sign = '-'
        octal = octal[1:]

    # Convert octal to binary
    binary = bin(int(octal, 8))[2:]

    # Convert binary to gray code
    gray = int(binary, 2) ^ (int(binary, 2) >> 1)

    # Return the gray code as a string, maintaining the sign magnitude notation
    return sign + bin(gray)[2:]