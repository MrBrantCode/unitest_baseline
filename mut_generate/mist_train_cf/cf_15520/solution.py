"""
QUESTION:
Write a function `find_palindromes(s)` that finds all unique palindromic substrings in a given string `s`. The function should consider both even and odd length palindromes. Return the list of unique palindromic substrings.
"""

def find_palindromes(s):
    # Helper function to expand around the center
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    palindromes = set()
    for i in range(len(s)):
        # Consider odd length palindromes
        expand_around_center(s, i, i)

        # Consider even length palindromes
        expand_around_center(s, i, i+1)

    return list(palindromes)