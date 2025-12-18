"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, ignoring non-alphanumeric characters, spaces, and case. If the string is not a palindrome, the function should return the longest palindrome substring. The function should handle special characters, numbers with leading zeros, and have a time complexity of O(n), where n is the length of the input string.
"""

import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    if s == s[::-1]:
        return True
    
    n = len(s)
    max_len = 0
    start = 0
    for i in range(n):
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left
            left -= 1
            right += 1
            
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left
            left -= 1
            right += 1
    
    if max_len > 1:
        return s[start:start+max_len]
    else:
        return False