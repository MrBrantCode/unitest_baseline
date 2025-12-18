"""
QUESTION:
Write a function named `transform_strings` that takes a string or a list of strings as input. The function should transform all alphabetic characters from the Latin alphabet to capital letters, ignoring any punctuation marks, digits, and special characters. If the input is a list of strings, the function should return a list of transformed strings.
"""

import string

def transform_strings(strings):
    """
    Transform all alphabetic characters from the Latin alphabet to capital letters,
    ignoring any punctuation marks, digits, and special characters.
    
    Args:
        strings (str or list of str): A string or a list of strings to be transformed.
    
    Returns:
        str or list of str: The transformed string or list of strings.
    """
    if isinstance(strings, str):
        strings = [strings]
    
    transformed_strings = []
    for s in strings:
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = ''.join([i for i in s if not i.isdigit()])
        s = ''.join([i for i in s if i.isalpha()])
        s = s.upper()
        transformed_strings.append(s)
    
    return transformed_strings if len(transformed_strings) > 1 else transformed_strings[0]