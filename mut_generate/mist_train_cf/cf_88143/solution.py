"""
QUESTION:
Create a function named `reverse_list` that takes a list of strings as input. The function should return a new list containing the reversed strings from the input list, excluding any strings that contain non-alphabetic characters or are palindromes.
"""

def reverse_list(list_of_strings):
    """
    Returns a new list containing the reversed strings from the input list, 
    excluding any strings that contain non-alphabetic characters or are palindromes.

    Args:
    list_of_strings (list): A list of strings

    Returns:
    list: A list of reversed strings
    """
    return [word[::-1] for word in list_of_strings if word.isalpha() and word != word[::-1]]