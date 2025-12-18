"""
QUESTION:
Create a function `number_to_binary(x: str, base: int)` that transforms an input number (string) of a given base (int) into its corresponding binary representation (string). The base can be 8 (octal), 10 (decimal), or 16 (hexadecimal). If the base is not one of these three, the function should return 'Invalid base'.
"""

def number_to_binary(x: str, base: int) -> str:
    """
    Transform an input number (string) of given base (int) into its corresponding binary representation (string).
    Base can be 8 (octal), 10 (decimal), or 16 (hexadecimal).
    
    Args:
        x (str): Input number as string.
        base (int): The base of the input number.
    
    Returns:
        str: The binary representation of the input number, or 'Invalid base' if the base is not 8, 10, or 16.
    """
    if base == 8:
        decimal_num = int(x, 8)
    elif base == 10:
        decimal_num = int(x, 10)
    elif base == 16:
        decimal_num = int(x, 16)
    else:
        return 'Invalid base'

    binary_num = bin(decimal_num)[2:]

    return binary_num