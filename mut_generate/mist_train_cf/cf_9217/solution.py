"""
QUESTION:
Write a function `get_palindromic_substrings(s)` that takes a string `s` as input and returns a list of all unique palindromic substrings in `s`. The function should handle both odd and even length palindromes.
"""

def get_palindromic_substrings(s):
    result = set()
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            result.add(s[left:right+1])
            left -= 1
            right += 1

    for i in range(n):
        expand_around_center(i, i)  # odd length palindromes
        expand_around_center(i, i+1)  # even length palindromes

    return list(result)