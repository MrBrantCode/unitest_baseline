"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that determines whether two input strings are anagrams without using built-in Python functions or libraries for string manipulation and sorting. The function should ignore whitespace characters and be case-insensitive.
"""

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    char_count1 = {}
    char_count2 = {}

    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if len(char_count1) != len(char_count2):
        return False

    for key in char_count1:
        if key not in char_count2 or char_count1[key] != char_count2[key]:
            return False

    return True