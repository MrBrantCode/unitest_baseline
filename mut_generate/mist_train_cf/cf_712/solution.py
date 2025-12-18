"""
QUESTION:
Write a function called `is_anagram` that takes two string parameters. The function should return `True` if the two input strings are anagrams of each other and `False` otherwise. The function should be case-sensitive and ignore any spaces or special characters. It should consider the frequency of each character in the strings and have a time complexity of O(n). The function should not use any built-in Python functions for sorting or counting characters.
"""

def is_anagram(str1, str2):
    # Remove spaces and special characters from both strings
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())
    
    # Create dictionaries to store frequency distribution
    freq1 = {}
    freq2 = {}
    
    # Update frequency distribution for str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    # Update frequency distribution for str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    # Compare the two dictionaries
    if freq1 == freq2:
        return True
    else:
        return False