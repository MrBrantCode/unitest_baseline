"""
QUESTION:
Write a function `binary_to_integer(binary_num)` that takes a string of binary digits as input and returns its equivalent integer value. The function should:

* Return `None` if the input string is empty or contains any characters other than '0', '1', or a single '-' at the beginning.
* Handle negative binary numbers by allowing a '-' character at the beginning of the string, in which case the function should return the equivalent negative integer value.
* Consider leading zeros in the binary string when converting it to an integer value.
* Implement a conversion algorithm that avoids using built-in functions or libraries to convert each binary digit to an integer.
"""

def binary_to_integer(binary_num):
    # Check for the validity of the binary string
    if not binary_num:
        return None
    for char in binary_num:
        if char != '0' and char != '1':
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