"""
QUESTION:
Create a function `is_anagram` that takes two strings as input. This function should remove any leading or trailing whitespace from both strings, convert them to lowercase, and check if the two strings are anagrams by sorting the alphabetic characters in both strings and comparing them. The function should return `True` if the sorted strings are equal and `False` otherwise. 

Restrictions: 
- If either string is empty, contains only whitespace, or contains non-alphabetic characters, the function should return `False`.
- If the input strings have different lengths, the function should return `False`, as they cannot be anagrams.
- If the input strings have the same letters but different frequencies, the function should return `False`, as they cannot be anagrams.
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
    
    # Sort both strings alphabetically
    sorted_str_1 = ''.join(sorted(str_1))
    sorted_str_2 = ''.join(sorted(str_2))
    
    # Check if the sorted strings are equal
    return sorted_str_1 == sorted_str_2