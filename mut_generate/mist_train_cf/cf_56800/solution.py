"""
QUESTION:
Write a function called `find_longest_palindrome` that takes a string `s` as input and returns the longest palindromic substring within it, considering the original case. If there are multiple longest palindromic substrings, return any of them.
"""

def find_longest_palindrome(s):
    if not s:
        return ''
    longest_palindrome = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:  # Check if it is a palindrome
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
    return longest_palindrome