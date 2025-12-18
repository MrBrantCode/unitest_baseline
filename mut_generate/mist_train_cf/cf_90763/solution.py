"""
QUESTION:
Write a function called `is_anagram` that takes two strings as input and returns `True` if the strings are anagrams of each other, and `False` otherwise. The function should ignore case and whitespace differences between the strings. It should not use any built-in string manipulation methods or libraries.
"""

def is_anagram(str1, str2):
    # Remove whitespaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Count the frequency of each character in the first string
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check if the second string has the same character frequency
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