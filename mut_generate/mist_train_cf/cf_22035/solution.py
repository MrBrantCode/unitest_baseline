"""
QUESTION:
Write a function `remove_vowels` that takes a string as input and returns the string without any vowels. The function should not use any built-in string manipulation functions or methods such as `replace()` or `translate()`, and should have a time complexity of O(n), where n is the length of the input string.
"""

def remove_vowels(input_string):
    """
    Removes all vowels from a given string.
    
    Args:
        input_string (str): The input string from which vowels need to be removed.
    
    Returns:
        str: The string without any vowels.
    """
    return ''.join([char for char in input_string if char.lower() not in ['a', 'e', 'i', 'o', 'u']])