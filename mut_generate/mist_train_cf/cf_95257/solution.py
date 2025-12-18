"""
QUESTION:
Write a function called `reverse_alpha_strings` that takes a list of strings as input, reverses each string that contains only alphabetic characters, and returns the list of reversed strings, ignoring any strings that contain special characters or numbers.
"""

def reverse_alpha_strings(strings):
    """
    Reverses each string that contains only alphabetic characters in the input list.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        list: A list of reversed strings, ignoring any strings that contain special characters or numbers.
    """
    return [word[::-1] for word in strings if word.isalpha()]