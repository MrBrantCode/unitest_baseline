"""
QUESTION:
Write a function `replace_first_occurrence` that takes a string `input_str`, a character `old_char`, and a character `new_char` as input. Replace the `old_char` with `new_char` in the first occurrence of each word in `input_str` without altering numbers or special symbols. The function should return the modified string.
"""

def replace_first_occurrence(input_str, old_char, new_char):
    """
    Replace the first occurrence of old_char with new_char in each word of input_str.
    
    Args:
        input_str (str): The input string.
        old_char (str): The character to be replaced.
        new_char (str): The character to replace with.
    
    Returns:
        str: The modified string.
    """
    words = input_str.split()
    modified_words = [word.replace(old_char, new_char, 1) for word in words]
    return ' '.join(modified_words)