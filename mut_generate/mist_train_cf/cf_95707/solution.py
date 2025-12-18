"""
QUESTION:
Implement the `is_anagram_and_palindrome` function, which takes two strings as parameters and returns a boolean value indicating if the strings are anagrams and palindromes. The function should ignore spaces, punctuation, and capitalization. It should return True if the strings are anagrams and palindromes, and False otherwise. The function should assume that the input strings only contain alphanumeric characters.
"""

import re

def is_anagram_and_palindrome(string1: str, string2: str) -> bool:
    # Remove spaces and punctuation, and convert to lowercase
    string1 = re.sub(r'[^a-zA-Z0-9]', '', string1.lower())
    string2 = re.sub(r'[^a-zA-Z0-9]', '', string2.lower())
    
    # Check if the modified strings are anagrams
    if sorted(string1) != sorted(string2):
        return False
    
    # Check if the modified strings are palindromes
    if string1 != string1[::-1] or string2 != string2[::-1]:
        return False
    
    # Return True if both conditions are satisfied
    return True