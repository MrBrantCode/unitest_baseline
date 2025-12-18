"""
QUESTION:
Create a function `convert_to_string` that takes an integer as input and returns its string representation using only bitwise operations. The function should not use any built-in string conversion functions or libraries. The integer will be a non-negative number.
"""

def convert_to_string(n):
    """
    Converts a non-negative integer to its string representation using only bitwise operations.

    Args:
        n (int): A non-negative integer.

    Returns:
        str: The string representation of the input integer.
    """
    string_variable = ''
    temp_variable = n
    while temp_variable != 0:
        digit = temp_variable & 0x0F
        char = digit + ord('0')
        string_variable = string_variable + chr(char)
        temp_variable = temp_variable // 10
    
    reversed_string = ''
    for char in reversed(string_variable):
        reversed_string += char

    return reversed_string