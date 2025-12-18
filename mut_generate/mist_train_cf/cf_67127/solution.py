"""
QUESTION:
Implement a function named `is_happy(s)` that determines whether a given string `s` is happy or not, where a happy string meets the following conditions: 
- it contains at least three characters
- every sequence of three consecutive characters is unique
- each individual character appears at least twice
- no character appears three times consecutively
- the string is not a palindrome.
"""

def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i:i+3] in s[i+3:]:
            return False
    if max(s.count(ch) for ch in set(s)) < 2 or min(s.count(ch) for ch in set(s)) < 2:
        return False
    if any(s[i-1] == s[i] == s[i+1] for i in range(1, len(s) - 1)):
        return False
    if s == s[::-1]:      # Check if string is a palindrome
        return False
    return True