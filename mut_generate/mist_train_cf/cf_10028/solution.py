"""
QUESTION:
Create a function `is_anagram(str1, str2)` that checks if two given strings are anagrams of each other. The function should return `True` if the strings are anagrams, and `False` otherwise. The strings should contain at least one vowel and one consonant. If either string is empty or does not meet these conditions, the function should return `False`. The comparison should be case-insensitive.
"""

def is_anagram(str1, str2):
    # Check if both strings are empty or have length less than 2
    if len(str1) < 2 or len(str2) < 2:
        return False
    
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Check if both strings contain at least one vowel and one consonant
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    if not (any(char in vowels for char in str1) and any(char in consonants for char in str1)):
        return False
    if not (any(char in vowels for char in str2) and any(char in consonants for char in str2)):
        return False
    
    # Check if both strings have the same characters (ignoring case)
    return sorted(str1) == sorted(str2)