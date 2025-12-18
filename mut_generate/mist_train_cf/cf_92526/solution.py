"""
QUESTION:
Write a function `is_anagram` that takes two strings as arguments and returns `True` if they are anagrams of each other, and `False` otherwise. The function should be case-insensitive, ignore any leading or trailing whitespace, and consider special characters. It should also return `False` if the input strings have different lengths.
"""

def is_anagram(s, t):
    # Remove leading and trailing whitespace
    s = s.strip()
    t = t.strip()
    
    # Convert the strings to lowercase
    s = s.lower()
    t = t.lower()
    
    # Check if the lengths are different
    if len(s) != len(t):
        return False
    
    # Count the occurrences of each character in both strings
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
    
    # If any count is not zero, the strings are not anagrams
    for char in count:
        if count[char] != 0:
            return False
    
    # If all counts are zero, the strings are anagrams
    return True