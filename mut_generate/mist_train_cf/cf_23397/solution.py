"""
QUESTION:
Write a function named `longest_palindromic_substring` to find the longest palindromic substring from a given character sequence. The function should take one string argument, which is the character sequence.
"""

def longest_palindromic_substring(s: str) -> str:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        longest_palindrome = max([longest_palindrome, palindrome1, palindrome2], key=len)

    return longest_palindrome