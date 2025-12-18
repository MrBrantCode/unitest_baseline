"""
QUESTION:
Write a function named `count_palindromic_substrings` that takes a string `s` as input and returns the number of unique palindromic substrings present in the string. A palindromic substring is a substring that reads the same forwards and backwards.
"""

def count_palindromic_substrings(s):
    count = set()
    n = len(s)

    # Check for odd length palindromes
    for i in range(n):
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            count.add(s[l:r + 1])
            l -= 1
            r += 1

    # Check for even length palindromes
    for i in range(n - 1):
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            count.add(s[l:r + 1])
            l -= 1
            r += 1

    return len(count)