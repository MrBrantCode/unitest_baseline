"""
QUESTION:
Write a function named `are_anagrams` that takes two strings `s1` and `s2` as input. The function should return True if `s1` and `s2` are anagrams and False otherwise. The function should be case-insensitive, ignore any spaces, punctuation, or special characters, and should not use any built-in functions for sorting, reversing, or transforming strings into another data type.
"""

def are_anagrams(s1, s2):
    # Normalize the strings
    s1 = ''.join(e for e in s1 if e.isalnum()).lower()
    s2 = ''.join(e for e in s2 if e.isalnum()).lower()

    # If the lengths of strings are different, they cannot be anagrams.
    if len(s1) != len(s2):
        return False

    # To store character counts
    count1 = [0] * 256
    count2 = [0] * 256

    # Increase count i in count1 and count2 for each character in s1 and s2
    for i in range(len(s1)):
        count1[ord(s1[i])] += 1
        count2[ord(s2[i])] += 1

    # If counts of characters are not the same, then s1 and s2 are not anagrams.
    for i in range(256): 
        if count1[i] != count2[i]:
            return False

    return True