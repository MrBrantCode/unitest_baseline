"""
QUESTION:
Write a function named `check_anagram` that takes two string arguments. The function should determine if the two strings are anagrams while ignoring non-alphabetical characters and considering only the alphabetical characters in a case-insensitive manner.
"""

def check_anagram(string1, string2):
    string1_filtered = ''.join(letter.lower() for letter in string1 if letter.isalpha())
    string2_filtered = ''.join(letter.lower() for letter in string2 if letter.isalpha())
    
    return sorted(string1_filtered) == sorted(string2_filtered)