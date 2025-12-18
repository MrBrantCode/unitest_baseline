"""
QUESTION:
Write a function `is_anagram(s1, s2)` that determines whether two input strings `s1` and `s2` are anagrams of each other, considering letter case, punctuation, and multi-word anagrams. The function should not use built-in sorting functions or libraries and should optimize for space complexity, minimizing the use of additional data structures. It should also minimize the number of iterations over the input strings, aiming for a time complexity of O(n), where n is the length of the longer string.
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