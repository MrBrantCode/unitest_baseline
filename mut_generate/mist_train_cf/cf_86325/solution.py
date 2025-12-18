"""
QUESTION:
Write a function `longest_palindrome` that takes a string as input and returns the longest palindromic substring with at least 5 characters, ignoring any whitespace or special characters. The function should have a time complexity of O(n^2) or better and should not use any built-in string manipulation functions.
"""

def longest_palindrome(s):
    s = ''.join(e for e in s if e.isalnum())
    longest = ""
    for i in range(len(s)):
        for j in range(i + 4, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest