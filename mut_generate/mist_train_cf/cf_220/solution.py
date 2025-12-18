"""
QUESTION:
Write a function `longest_palindrome` that takes a string as input and returns the longest palindromic substring with at least 5 characters, ignoring any whitespace or special characters. The function should not use any built-in string manipulation functions like `reverse()` or `substring()` and should have a time complexity of O(n^2) or better.
"""

def longest_palindrome(s):
    def is_palindrome(string):
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    s = ''.join(e for e in s if e.isalnum())
    longest = ""
    for i in range(len(s)):
        for j in range(i + 4, len(s)):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest