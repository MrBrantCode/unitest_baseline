"""
QUESTION:
Implement a function `is_anagram_and_palindrome(string1: str, string2: str) -> bool` that takes two strings as parameters, removes all non-alphanumeric characters and converts to lowercase, and returns a boolean value indicating if the modified strings are both anagrams and palindromes.
"""

import re

def is_anagram_and_palindrome(string1: str, string2: str) -> bool:
    # Step 1: Convert both strings to lowercase and remove spaces, punctuation, and special characters
    string1 = re.sub(r'[^a-zA-Z0-9]', '', string1.lower())
    string2 = re.sub(r'[^a-zA-Z0-9]', '', string2.lower())
    
    # Step 2: Check if the modified strings are anagrams
    if sorted(string1) != sorted(string2):
        return False
    
    # Step 3: Check if the modified strings are palindromes
    if string1 != string1[::-1]:
        return False
    
    # Step 4: Return True if both conditions are satisfied
    return True