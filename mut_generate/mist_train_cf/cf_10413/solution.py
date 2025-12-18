"""
QUESTION:
Write a function `convert_string_to_int(s: str, multiplier: int) -> int:` that takes a string `s` and an integer `multiplier` as input, and returns the sum of the ASCII values of all characters in the string, multiplied by the given multiplier. The string `s` consists of alphabetic and/or punctuation characters, with a length between 1 and 10^5, and the multiplier is an integer between 1 and 1000.
"""

def convert_string_to_int(s: str, multiplier: int) -> int:
    """
    This function calculates the sum of ASCII values of all characters in a string, 
    multiplied by a given multiplier.

    Args:
    s (str): The input string consisting of alphabetic and/or punctuation characters.
    multiplier (int): The multiplier to multiply the sum of ASCII values with.

    Returns:
    int: The sum of ASCII values of all characters in the string, multiplied by the given multiplier.
    """
    total = 0
    for ch in s:
        total += ord(ch)
    return total * multiplier