"""
QUESTION:
Write a function `lengthOfLongestSubstring(s, n)` that returns the length of the longest substring of string `s` that contains exactly `n` distinct characters. The function takes two parameters: a string `s` and an integer `n`. The length of string `s` is between 1 and 50,000, and the value of `n` is between 0 and 50.
"""

def lengthOfLongestSubstring(s, n):
    if n == 0:
        return 0
    left = 0
    unique_chars = 0
    max_len = 0
    char_count = {}
    for right in range(len(s)):
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1
            unique_chars += 1
        while unique_chars > n:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                unique_chars -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len