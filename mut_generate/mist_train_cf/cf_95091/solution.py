"""
QUESTION:
Write a function `count_vowels` that takes a string as input, removes all non-alphabetical characters, converts all uppercase letters to lowercase, and returns the count of vowels remaining. The function should only consider the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

import re

def count_vowels(s):
    """
    This function takes a string as input, removes all non-alphabetical characters, 
    converts all uppercase letters to lowercase, and returns the count of vowels remaining.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The count of vowels in the string.
    """
    
    # Remove non-alphabetical characters
    s = re.sub("[^a-zA-Z]", "", s)
    
    # Convert uppercase letters to lowercase
    s = s.lower()
    
    # Count the number of vowels
    vowels = "aeiou"
    count = sum(1 for char in s if char in vowels)
    
    return count