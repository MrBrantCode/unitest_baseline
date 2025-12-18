"""
QUESTION:
Write a function `longest_palindrome(string)` that finds the longest palindromic substring in a given string. The function should return the longest palindromic substring. There are no restrictions on the input string, and it can contain spaces and punctuation.
"""

def entrance(s):
    n = len(s)
    max_length = 0
    start = 0

    for i in range(n):
        # check for odd-length palindromes
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # check for even-length palindromes
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_length]