"""
QUESTION:
Create a function named `is_anagram` that takes two strings as input, `s1` and `s2`, and returns a boolean value indicating whether they are anagrams of each other. The function should ignore any whitespace characters and be case insensitive.
"""

def is_anagram(s1, s2):
    # Remove whitespace characters and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort the strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    # Compare the sorted strings
    return sorted_s1 == sorted_s2