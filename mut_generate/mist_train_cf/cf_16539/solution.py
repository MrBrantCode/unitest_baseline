"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks whether string `s1` is an anagram of string `s2`, taking into account letter case and punctuation, and handling multi-word anagrams. The function should return `True` if `s1` is an anagram of `s2` and `False` otherwise.
"""

import string

def entance(s1, s2):
    # Remove punctuation and convert to lowercase
    s1 = s1.translate(str.maketrans('', '', string.punctuation)).lower()
    s2 = s2.translate(str.maketrans('', '', string.punctuation)).lower()

    # Count the frequency of each character in s1
    s1_freq = {}
    for char in s1:
        if char.isalpha():
            s1_freq[char] = s1_freq.get(char, 0) + 1

    # Check if the frequency of each character in s1 matches the frequency in s2
    for char in s2:
        if char.isalpha():
            if char not in s1_freq:
                return False
            s1_freq[char] -= 1
            if s1_freq[char] == 0:
                del s1_freq[char]

    # If all characters have been accounted for, s1 is an anagram of s2
    return len(s1_freq) == 0