"""
QUESTION:
Write a function `longest_pleasant_substring(s)` that takes a string `s` of length between 1 and 100, composed of uppercase and lowercase English letters. The function should return the longest 'pleasant' substring, where a substring is classified as 'pleasant' if it contains every alphabet character in both uppercase and lowercase versions. If there are multiple 'pleasant' substrings of the same length, return the one that occurs first. If there are no 'pleasant' substrings, return an empty string.
"""

def longest_pleasant_substring(s):
    n = len(s)
    longest_substr = ''
    for i in range(n):
        for j in range(i+2, n+1): 
            substr = s[i:j]
            if is_pleasant(substr) and len(substr) > len(longest_substr):
                longest_substr = substr
    return longest_substr

def is_pleasant(s):
    lower, upper = set(), set()
    for c in s:
        if c.islower():
            lower.add(c)
        else:
            upper.add(c.lower())
    return lower == upper