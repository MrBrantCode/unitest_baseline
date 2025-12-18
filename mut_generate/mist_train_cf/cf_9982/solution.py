"""
QUESTION:
Write a function called longest_substring() that takes a string as input and returns the longest substring without repeating characters, containing at least one uppercase letter and one special character.
"""

def longest_substring(s):
    max_len = 0
    max_str = ""
    has_upper = False
    has_special = False
    left = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        has_upper = has_upper or s[right].isupper()
        has_special = has_special or not s[right].isalnum()
        if has_upper and has_special and right - left + 1 > max_len:
            max_len = right - left + 1
            max_str = s[left:right + 1]
    return max_str