"""
QUESTION:
Write a function `longest_palindrome(s)` that takes a string `s` as input and returns the longest palindrome substring with at least 3 characters, ignoring any whitespace or special characters, without using built-in string manipulation functions or libraries. The function should be case-insensitive.
"""

def longest_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i+2, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 3 and len(substring) > len(max_palindrome):
                max_palindrome = substring
    return max_palindrome