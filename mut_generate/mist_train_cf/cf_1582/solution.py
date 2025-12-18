"""
QUESTION:
Write a function named `is_anagram` that takes two strings `s1` and `s2` as input, and returns `True` if `s1` is an anagram of `s2` and `False` otherwise. The function should consider letter case and punctuation, handle multi-word anagrams, and optimize for space complexity with a time complexity of O(n), where n is the length of the longer string. The function should not use any built-in sorting functions or libraries to check for anagrams.
"""

def is_anagram(s1, s2):
    # Preprocess the strings
    s1 = ''.join(ch.lower() for ch in s1 if ch.isalnum())
    s2 = ''.join(ch.lower() for ch in s2 if ch.isalnum())

    # Create a character count dictionary
    char_count = {}

    # Increment count for characters in s1
    for ch in s1:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Decrement count for characters in s2
    for ch in s2:
        char_count[ch] = char_count.get(ch, 0) - 1

    # Check if all character counts are zero
    return all(count == 0 for count in char_count.values())