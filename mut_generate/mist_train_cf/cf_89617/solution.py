"""
QUESTION:
Create a function named `binary_to_integer` that takes a string `binary_num` as input and returns its equivalent integer value.

The `binary_num` string must consist only of '0' and '1' characters and must not be empty. If these conditions are not met, the function should return `None`.

The `binary_num` string may start with a '-' character to indicate a negative number, in which case the function should return the equivalent negative integer value. The '-' character should only appear at the beginning of the string.

The function should also handle leading zeros in the `binary_num` string by considering them when converting the string to an integer value.

The conversion algorithm should not use any built-in functions or libraries, and should be implemented manually.
"""

def binary_to_integer(binary_num):
    # Check for the validity of the binary string
    if not binary_num:
        return None
    for char in binary_num:
        if char != '0' and char != '1' and char != '-':
            return None
    
    # Handle negative binary numbers
    if binary_num[0] == '-':
        if len(binary_num) == 1:
            return None
        if any(char != '0' and char != '1' for char in binary_num[1:]):
            return None
        return -1 * binary_to_integer(binary_num[1:])
    
    # Handle leading zeros
    binary_num = binary_num.lstrip('0')
    if not binary_num:
        return 0
    
    # Optimize the conversion algorithm
    result = 0
    for char in binary_num:
        result = (result << 1) + (ord(char) - ord('0'))
    
    return result