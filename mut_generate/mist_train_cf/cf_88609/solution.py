"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two input strings are anagrams. The function should consider both uppercase and lowercase letters, ignore special characters and numbers, and handle empty strings. Both input strings should have a length of at least 2. Return True if the strings are anagrams, False otherwise.
"""

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())
    
    if len(s1) < 2 or len(s2) < 2:
        return False
    
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))
    
    return s1_list == s2_list