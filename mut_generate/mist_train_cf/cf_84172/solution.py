"""
QUESTION:
Create a function named `vowels_count(s)` that takes a string `s` as input and returns the total count of vowels it contains. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' if it appears at the end of the input word. The function should be case-insensitive and handle unusual characters within the input string. It should also handle edge cases such as an empty input string.
"""

import re

def vowels_count(s):
    """
    This function takes a string representing a word as an argument and 
    returns the total number of all vowels it contains.
    The vowels considered here are 'a', 'e', 'i', 'o', 'u', and 'y' if it appears at the end of the word.
    The function ignores case sensitivity and carefully handles unusual characters within the input string.
    """
    
    # Checking for empty string
    if not s:
        return 0

    s = s.lower()  # convert string in lower case to remove case sensitivity
    pattern = re.compile(r'[aeiou]|y$')  # pattern to match vowels and y at the end

    return len(pattern.findall(s))  # return count of matched vowels 