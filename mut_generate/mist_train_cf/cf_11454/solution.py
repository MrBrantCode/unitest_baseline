"""
QUESTION:
Write a function called `convert_base` that takes three parameters: `digits`, `from_base`, and `to_base`, where `digits` is a string of numbers, `from_base` is the base of the input string, and `to_base` is the desired base to convert to. The function should convert the input string from the `from_base` to the `to_base` and return the converted string. Both `from_base` and `to_base` should be positive integers between 2 and 36. The function should also handle cases where `digits` contains non-numeric characters for bases 2-9 and non-alphabetic characters A-Z for bases 11-36.
"""

def convert_base(digits, from_base, to_base):
    """
    Converts a number from a given base to another base.

    Args:
        digits (str): The number to be converted.
        from_base (int): The base of the input number.
        to_base (int): The desired base to convert to.

    Returns:
        str: The converted number in the desired base.
    """
    decimal = int(digits, from_base)
    converted = ""
    
    while decimal > 0:
        remainder = decimal % to_base
        if remainder < 10:
            converted = str(remainder) + converted
        else:
            converted = chr(remainder - 10 + ord('A')) + converted
        decimal //= to_base
    
    return converted