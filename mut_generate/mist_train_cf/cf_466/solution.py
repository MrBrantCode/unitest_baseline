"""
QUESTION:
Write a function `find_palindromic_substrings(s)` that takes a string `s` as input and returns a set of all unique palindromic substrings of `s` (including both even and odd length palindromes), excluding any substrings consisting of only repeating characters.
"""

def find_palindromic_substrings(s):
    result = set()
    n = len(s)

    # Helper function to check if a substring is a palindrome
    def is_palindrome(substring):
        return substring == substring[::-1]

    # Check for all palindromic substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if len(set(substring)) > 1 and is_palindrome(substring):
                result.add(substring)

    return result