"""
QUESTION:
Write a function `is_anagram` that determines if two input strings are anagrams of each other, ignoring case, spaces, and punctuation marks, and return True if they are anagrams, False otherwise.
"""

import string

def is_anagram(string1, string2):
    # Remove spaces and punctuation marks
    string1 = string1.translate(str.maketrans("", "", string.punctuation + " "))
    string2 = string2.translate(str.maketrans("", "", string.punctuation + " "))
    
    # Convert to lowercase
    string1 = string1.lower()
    string2 = string2.lower()
    
    # Sort the strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    
    # Compare the sorted strings
    return sorted_string1 == sorted_string2