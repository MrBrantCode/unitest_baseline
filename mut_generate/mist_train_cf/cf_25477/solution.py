"""
QUESTION:
Write a function `remove_character(var_str, n)` to remove the nth index character from a nonempty string `var_str`. The function should take two parameters: `var_str` (the input string) and `n` (the index of the character to be removed), and return the resulting string. The index `n` is 0-based, meaning the first character of the string has an index of 0.
"""

def remove_character(var_str, n):
    """
    Removes the nth index character from a nonempty string.

    Args:
    var_str (str): The input string.
    n (int): The index of the character to be removed (0-based).

    Returns:
    str: The resulting string after removing the nth index character.
    """
    first_part = var_str[:n] 
    last_part = var_str[n+1:]
    return first_part + last_part