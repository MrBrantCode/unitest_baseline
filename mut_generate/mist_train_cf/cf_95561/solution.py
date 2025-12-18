"""
QUESTION:
Create a function named `is_anagram` that takes two strings as input and checks if they are anagrams of one another. The function should ignore spaces, punctuation marks, and be case-insensitive. It should efficiently handle large input strings with lengths up to 10^6 characters. The function should return True if the strings are anagrams, and False otherwise.
"""

import string

def is_anagram(str1, str2):
    # Remove spaces and punctuation marks, and convert to lowercase
    str1 = str1.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    str2 = str2.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Count the frequency of each character in str1
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check if the frequency of each character in str1 is the same in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    
    # Check if all character frequencies are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True