"""
QUESTION:
Write a function `isAnagram` that takes two strings as input and returns a boolean value indicating if the two strings are anagrams of each other. The function should also check if the anagram contains at least one vowel and one consonant. The input strings may contain spaces and can be a mix of uppercase and lowercase letters. Return `False` if both strings are empty or do not meet the required conditions.
"""

def entrance(str1, str2):
    # Check if both strings are empty
    if not str1 and not str2:
        return False
    
    # Convert the strings to lowercase and remove any spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Check if both strings contain at least one vowel and one consonant
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    has_vowel_str1 = False
    has_consonant_str1 = False
    has_vowel_str2 = False
    has_consonant_str2 = False
    
    for char in str1:
        if char in vowels:
            has_vowel_str1 = True
        elif char in consonants:
            has_consonant_str1 = True
        
    for char in str2:
        if char in vowels:
            has_vowel_str2 = True
        elif char in consonants:
            has_consonant_str2 = True
    
    if not (has_vowel_str1 and has_consonant_str1 and has_vowel_str2 and has_consonant_str2):
        return False
    
    # Check if the strings are anagrams of each other
    return sorted(str1) == sorted(str2)