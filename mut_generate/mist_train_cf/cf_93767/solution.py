"""
QUESTION:
Write a function named `find_palindromes(s)` that takes a string `s` as input and returns a list of all unique palindromic substrings in the string, considering both odd and even length palindromes. The function should not take any other parameters besides the input string `s`.
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