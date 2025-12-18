"""
QUESTION:
Write a function `is_anagram(str1, str2)` to check if two input strings are anagrams of each other. The function should have a time complexity of O(n) where n is the length of the input strings. It cannot use built-in functions or libraries for sorting or manipulating strings. The function should return `True` if the strings are anagrams, and `False` otherwise.
"""

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}

    # Count the frequency of characters in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract the frequency of characters in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # Check if all character frequencies are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True