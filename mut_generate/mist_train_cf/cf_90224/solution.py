"""
QUESTION:
Write a function `count_palindromic_substrings(s)` that takes a string `s` as input and returns the number of unique palindromic substrings in `s`. A palindromic substring is a substring that reads the same forwards and backwards. Note that a single character is considered a palindrome.
"""

def count_palindromic_substrings(s):
    count = set()

    # Check for odd length palindromes
    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count.add(s[l:r + 1])
            l -= 1
            r += 1

    # Check for even length palindromes
    for i in range(len(s) - 1):
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count.add(s[l:r + 1])
            l -= 1
            r += 1

    return len(count)