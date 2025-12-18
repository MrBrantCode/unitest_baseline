"""
QUESTION:
Write a function `firstUniqChar` that takes a non-empty string `s` consisting of lowercase English letters as input and returns the index of the first non-repeating character in the string. If there are no non-repeating characters, return -1.
"""

def firstUniqChar(s: str) -> int:
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1  # No non-repeating character found