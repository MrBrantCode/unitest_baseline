"""
QUESTION:
Write a function named `get_palindromic_substrings(s)` that takes a string `s` as input and returns a list of all unique palindromic substrings in `s`. A palindromic substring is a substring that reads the same backward as forward. The function should consider both odd and even length palindromic substrings.
"""

def get_palindromic_substrings(s):
    result = []
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            result.append(s[left:right+1])
            left -= 1
            right += 1

    for i in range(n):
        expand_around_center(i, i)  # odd length palindromes
        expand_around_center(i, i+1)  # even length palindromes

    return result