"""
QUESTION:
Create a function `is_anagram(string1, string2)` that determines whether two input strings are anagrams of each other. The function should be case-insensitive and ignore leading and trailing white spaces in the strings. Return a boolean value indicating whether the strings are anagrams.
"""

def is_anagram(string1, string2):
    # Convert strings to lowercase and remove leading/trailing whitespaces
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()
    
    # Sort the characters in the strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    
    # Compare the sorted strings
    return sorted_string1 == sorted_string2