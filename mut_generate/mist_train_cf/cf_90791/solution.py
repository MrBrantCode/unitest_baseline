"""
QUESTION:
Write a function called `longest_palindromic_substring` that takes a string `s` as input and returns the longest palindromic substring. The function should handle strings of up to 1000 characters.
"""

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s
    
    start, end = 0, 0
    for i in range(len(s)):
        # Case 1: odd-length palindromic substring
        l1 = expand_around_center(s, i, i)
        # Case 2: even-length palindromic substring
        l2 = expand_around_center(s, i, i + 1)
        length = max(l1, l2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1