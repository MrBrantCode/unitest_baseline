"""
QUESTION:
Write a function `is_anagram_and_palindrome(string1: str, string2: str) -> bool` that takes in two strings as parameters and returns a boolean value indicating if the strings are both anagrams and palindromes, ignoring spaces, punctuation, and capitalization.
"""

import re

def is_anagram_and_palindrome(string1: str, string2: str) -> bool:
    # Convert both strings to lowercase and remove spaces, punctuation, and special characters
    string1 = re.sub(r'[^a-zA-Z0-9]', '', string1.lower())
    string2 = re.sub(r'[^a-zA-Z0-9]', '', string2.lower())
    
    # Check if the modified strings are anagrams
    if sorted(string1) != sorted(string2):
        return False
    
    # Check if the modified strings are palindromes
    if string1 != string1[::-1]:
        return False
    
    # Return True if both conditions are satisfied
    return True