"""
QUESTION:
Implement the function `longest_substring_without_repeating_characters(s)` to find the length of the longest substring in a given string `s` without repeating characters. The input string `s` consists of only English letters. The function should have a time complexity of O(n) where n is the length of the string.
"""

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result