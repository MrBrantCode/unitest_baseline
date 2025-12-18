"""
QUESTION:
Write a function called `longest_substring` that takes a string as input and returns the length of the longest substring with non-repeating characters.
"""

def longest_substring(s):
    max_length = 0
    char_set = set()
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length