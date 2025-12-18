"""
QUESTION:
Write a function named `longest_substring` that takes a string `s` as input and returns the longest substring without any repeated characters. The function should update its `start` pointer to the character right after the repeated character and return the longest substring instead of its length.
"""

def longest_substring(s):
    maxLength = 0
    start = 0
    char_dict = {}
    result = ""
    for i, char in enumerate(s):
        if char in char_dict and char_dict[char] >= start:
            maxLength = max(maxLength, i - start)
            if maxLength == i - start:
                result = s[start:i]
            start = char_dict[char] + 1
        char_dict[char] = i
    if maxLength < len(s) - start:
        result = s[start:]
    return result