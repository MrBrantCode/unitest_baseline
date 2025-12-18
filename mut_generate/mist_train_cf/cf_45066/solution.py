"""
QUESTION:
Write a function named `hex_to_decimal` that takes a string representing a hexadecimal number as input and returns its equivalent decimal representation. The function should manually convert the hexadecimal to decimal without using any built-in hex-to-decimal conversion functions. It should also validate if the given string is a valid hexadecimal. If the input string is not a valid hexadecimal, the function should return None. The input string may or may not have the "0x" prefix, and the prefix may be in lowercase or uppercase.
"""

def hex_to_decimal(hex_value):
    """
    This function takes a string representing a hexadecimal number as input 
    and returns its equivalent decimal representation. It manually converts 
    the hexadecimal to decimal without using any built-in hex-to-decimal 
    conversion functions. It also validates if the given string is a valid 
    hexadecimal. If the input string is not a valid hexadecimal, the 
    function returns None.
    
    Parameters:
    hex_value (str): A string representing a hexadecimal number.
    
    Returns:
    int or None: The decimal representation of the hexadecimal number, or None if the input is not a valid hexadecimal.
    """
    
    # Remove the '0x' or '0X' prefix if it exists
    hex_value = hex_value[2:] if hex_value.lower().startswith('0x') else hex_value
    
    decimal_value = 0
    for i, digit in enumerate(hex_value[::-1]):
        if '0' <= digit <= '9':
            value = int(digit)
        elif 'a' <= digit.lower() <= 'f':
            value = ord(digit.lower()) - ord('a') + 10
        else:
            return None  # Return None if the input is not a valid hexadecimal

        decimal_value += value * (16 ** i)
    
    return decimal_value