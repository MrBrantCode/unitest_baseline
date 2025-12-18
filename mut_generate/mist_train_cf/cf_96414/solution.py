"""
QUESTION:
Write a function named `is_anagram` that takes two strings `str1` and `str2` as input and returns a boolean value indicating whether the strings are anagrams. The function must be case-insensitive, have a time complexity of O(n), where n is the length of the longer string, and have a space complexity of O(1).
"""

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    char_count = {}

    for char in str1:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char.isalpha():
            if char not in char_count:
                return False
            char_count[char] -= 1

    for count in char_count.values():
        if count != 0:
            return False

    return True