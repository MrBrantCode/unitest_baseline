"""
QUESTION:
Implement a function `string_to_integer(s)` that takes a string `s` as input and returns its corresponding integer value. The string may contain a leading '+' or '-' sign, but only contains digits otherwise. If the string cannot be converted to an integer, return 0. The integer result should be within the range of -2^31 to 2^31 - 1.
"""

def string_to_integer(s):
    # Remove leading and trailing whitespaces
    s = s.strip()

    # Check if the string is empty
    if len(s) == 0:
        return 0

    # Check if the first character is a valid sign
    if s[0] == '+' or s[0] == '-':
        sign = -1 if s[0] == '-' else 1
        s = s[1:]
    else:
        sign = 1

    # Convert the string to an integer
    result = 0
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            return 0

    # Apply the sign to the result
    result *= sign

    # Check if the result is within the valid range
    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result