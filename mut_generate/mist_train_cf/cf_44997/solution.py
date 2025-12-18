"""
QUESTION:
Create a function named `enhanced_binary_conversion` that takes a string `y` as input. This function should convert the binary string into its octal representation if the string length is even, and into its hexadecimal representation if the string length is odd. The function should not use any built-in or library functions. If the input string starts with more than one '0', only the relevant part of the string starting from the first '1' should be converted. The function should also handle error cases where the input string is not a valid binary string.
"""

def enhanced_binary_conversion(y: str) -> str:
    # Check for leading zeros and adjust the binary string
    if len(y) > 1 and y[0] == '0':
        idx = y.find('1')
        y = y[idx:]

    # Validate whether the string is binary or not
    if all([c in '01' for c in y]):
        # Calculate the integer value
        decNum = 0
        for i in range(len(y)):
            decNum = decNum * 2 + int(y[i])

        # Create a lookup table for conversion
        octTable = '01234567'
        hexTable = '0123456789ABCDEF'

        # Calculate the hexadecimal or octal representation
        if len(y) % 2 == 0:
            # For even lengths, convert into octal
            result = ""
            while decNum > 0:
                result = octTable[decNum % 8] + result
                decNum //= 8
        else:
            # For odd lengths, convert into hexadecimal
            result = ""
            while decNum > 0:
                result = hexTable[decNum % 16] + result
                decNum //= 16

        return result
    else:
        # Return error message when input is not binary
        return "Invalid binary string"