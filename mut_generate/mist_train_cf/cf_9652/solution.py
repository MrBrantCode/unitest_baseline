"""
QUESTION:
Create a function named `are_anagrams` that takes two strings `str1` and `str2` as input and returns a boolean value indicating whether they are anagrams of each other. The function should be case-sensitive, handle whitespace characters by ignoring them, and consider only alphanumeric characters. It should also have a time complexity of O(n), where n is the length of the longer string.
"""

def are_anagrams(str1, str2):
    # Remove whitespace characters and convert to original case-sensitive condition
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())
    
    # Check if lengths are equal
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store character frequencies
    freq1 = {}
    freq2 = {}
    
    # Count character frequencies in str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    # Count character frequencies in str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    # Compare the dictionaries
    if freq1 == freq2:
        return True
    else:
        return False