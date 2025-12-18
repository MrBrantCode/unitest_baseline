"""
QUESTION:
Write a function named `longest_palindrome` that takes a string `s` as input and returns the longest palindromic substring from `s`. The function must not use any built-in string manipulation functions such as `reverse()` or slicing.
"""

def longest_palindrome(s):
    def is_palindrome(substring):
        left = 0
        right = len(substring) - 1
        while left < right:
            if substring[left] != substring[right]:
                return False
            left += 1
            right -= 1
        return True

    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = ""
            for k in range(i, j+1):
                substring += s[k]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest