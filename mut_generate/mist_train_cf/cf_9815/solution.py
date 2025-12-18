"""
QUESTION:
Write a function `replace_letters` that replaces all occurrences of a letter `old_letter1` with `new_letter1` and all occurrences of another letter `old_letter2` with `new_letter2` in a given string `input_string`. The function should return the modified string.
"""

def replace_letters(input_string, old_letter1, new_letter1, old_letter2, new_letter2):
    """
    Replaces all occurrences of two letters in a given string with new letters.
    
    Args:
    input_string (str): The input string to be modified.
    old_letter1 (str): The first letter to be replaced.
    new_letter1 (str): The replacement for the first letter.
    old_letter2 (str): The second letter to be replaced.
    new_letter2 (str): The replacement for the second letter.
    
    Returns:
    str: The modified string.
    """
    return input_string.replace(old_letter1, new_letter1).replace(old_letter2, new_letter2)