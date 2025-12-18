"""
QUESTION:
Write a function `find_palindromic_substrings` that finds all non-empty palindromic substrings of a given string. The function should return a list of all unique non-empty palindromic substrings in no particular order. The input string will only contain lowercase English letters.
"""

def find_palindromic_substrings(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring:
                palindromes.add(substring)
    return list(palindromes)