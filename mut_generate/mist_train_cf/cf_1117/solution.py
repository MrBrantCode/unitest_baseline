"""
QUESTION:
Create a function named `is_anagram` that takes two strings as arguments and checks if they are anagrams by returning True if they contain the same letters with the same frequency, and False otherwise. The function should ignore case, whitespace, and non-alphabetic characters, and should return False if either string is empty, contains only whitespace, or has different lengths.
"""

def is_anagram(str_1, str_2):
    # Remove leading/trailing whitespace and convert to lowercase
    str_1 = str_1.strip().lower()
    str_2 = str_2.strip().lower()
    
    # Check if either string is empty or contains only whitespace
    if not str_1 or not str_2:
        return False
    
    # Check if either string contains non-alphabetic characters
    if not str_1.isalpha() or not str_2.isalpha():
        return False
    
    # Check if the strings have different lengths
    if len(str_1) != len(str_2):
        return False
    
    # Remove non-alphabetic characters from both strings
    str_1 = ''.join(c for c in str_1 if c.isalpha())
    str_2 = ''.join(c for c in str_2 if c.isalpha())
    
    # Sort both strings alphabetically
    sorted_str_1 = ''.join(sorted(str_1))
    sorted_str_2 = ''.join(sorted(str_2))
    
    # Check if the sorted strings are equal
    if sorted_str_1 == sorted_str_2:
        return True
    
    return False