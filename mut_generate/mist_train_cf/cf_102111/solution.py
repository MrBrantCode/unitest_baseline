"""
QUESTION:
Write a function `is_palindrome_and_count_unique_chars(s)` that checks if a given string `s` is a palindrome and counts the number of unique characters in the string. The function should disregard spaces, punctuation, and capitalization, and should remove any non-alphanumeric characters before checking for palindrome. It should return a tuple containing a boolean indicating whether the string is a palindrome and the number of unique characters in the string.
"""

import string

def is_palindrome_and_count_unique_chars(s):
    """
    Checks if a given string is a palindrome and counts the number of unique characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    tuple: A tuple containing a boolean indicating whether the string is a palindrome and the number of unique characters.
    """
    # Remove non-alphanumeric characters
    cleaned_s = ''.join(c for c in s if c.isalnum())
    
    # Convert to lowercase for case-insensitive comparison
    cleaned_s = cleaned_s.lower()
    
    # Check if the string is a palindrome
    is_palindrome = cleaned_s == cleaned_s[::-1]
    
    # Count the number of unique characters
    unique_chars = len(set(cleaned_s))
    
    return is_palindrome, unique_chars