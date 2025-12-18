"""
QUESTION:
Write a function named `longest_palindrome` that takes a string as input and returns the longest palindromic substring. The function should consider both odd-length and even-length palindromes.
"""

def longest_palindrome(string):
    n = len(string)
    max_length = 0
    start = 0

    for i in range(n):
        # check for odd-length palindromes
        left = right = i
        while left >= 0 and right < n and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # check for even-length palindromes
        left = i
        right = i + 1
        while left >= 0 and right < n and string[left] == string[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return string[start:start + max_length]