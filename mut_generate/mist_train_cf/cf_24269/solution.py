"""
QUESTION:
Write a function `is_anagram(string1, string2)` that checks if two input strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. The strings may contain any characters, and the comparison should be case-sensitive. The function should not use any built-in sorting functions or libraries.
"""

def is_anagram(string1, string2):
    # Make sure strings are the same length
    if len(string1) != len(string2):
        return False

    # Create dictionary of letter frequency for each string 
    char_freq1 = {}
    char_freq2 = {}

    # Iterate through each character in the strings
    for char in string1:
        char_freq1[char] = char_freq1.get(char, 0) + 1
    for char in string2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    # Compare the two dictionaries
    return char_freq1 == char_freq2