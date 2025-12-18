"""
QUESTION:
Write a function `process_string` that takes a string of at least 3 characters and a specific character as input. The function should return a tuple containing the second character of the string, a boolean indicating whether the string is a palindrome, and a list of all positions where the specific character appears in the string.
"""

def process_string(s, char):
    """
    Returns a tuple containing the second character of the string, 
    a boolean indicating whether the string is a palindrome, 
    and a list of all positions where the specific character appears in the string.

    Args:
        s (str): The input string of at least 3 characters.
        char (str): The specific character.

    Returns:
        tuple: A tuple containing the second character, 
               a boolean indicating whether the string is a palindrome, 
               and a list of all positions where the specific character appears.
    """
    second_char = s[1]
    is_palindrome = s == s[::-1]
    positions = [i for i in range(len(s)) if s[i] == char]
    return (second_char, is_palindrome, positions)