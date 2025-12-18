"""
QUESTION:
Write a function named `hex_to_int` that takes a hexadecimal string as input and returns its corresponding integer value. The input string will only contain characters from 0-9 and A-F (both uppercase and lowercase). The function should handle both lowercase and uppercase hexadecimal characters.
"""

def hex_to_int(hex_string):
    # Convert the hexadecimal string to uppercase
    hex_string = hex_string.upper()

    # Initialize the result
    result = 0

    # Iterate through each character in the hexadecimal string
    for char in hex_string:
        # Convert the character to its decimal value
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10

        # Shift the result left by 4 bits and add the decimal value of the character
        result = (result << 4) + value

    return result