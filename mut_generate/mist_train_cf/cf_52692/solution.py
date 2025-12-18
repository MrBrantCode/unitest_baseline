"""
QUESTION:
Create a function `replace_and_reverse` that takes a string `s` as input, replaces every second character in the string with "X", and then reverses the order of characters. The function should return the resulting string.
"""

def replace_and_reverse(s):
    """
    Replace every second character in the string with "X" and then reverse the order of characters.

    Args:
        s (str): The input string.

    Returns:
        str: The resulting string with every second character replaced with "X" and reversed.
    """
    # Replace every second character with "X"
    result = "".join(c if i % 2 == 0 else "X" for i, c in enumerate(s))
    
    # Reverse the order of characters
    result = result[::-1]
    
    return result