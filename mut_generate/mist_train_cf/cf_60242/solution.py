"""
QUESTION:
Write a function `longest_palin_substring(text)` that takes a string `text` as input and returns the longest palindromic substring. The function should be able to handle strings of any length, and the input string is not guaranteed to contain any palindromes. The function should return the longest contiguous substring that reads the same backwards as forwards.
"""

def longest_palin_substring(text):
    n = len(text)
    table = [[0 for x in range(n)]for y in range(n)]

    # All substrings of length 1 are palindromes
    maxLength = 1
    i = 0
    while (i < n):
        table[i][i] = True
        i = i + 1

    # check for substring of length 2
    start = 0
    i = 0
    while i < n - 1:
        if (text[i] == text[i + 1]):
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    # Check for lengths greater than 2
    cl = 3
    while cl <= n:
        i = 0
        while i < (n - cl + 1):
            # Get the ending index of substring from
            # starting index i and length cl
            j = i + cl - 1

            # checking for sub-string from i'th index to
            # j'th index iff str[i+1] to str[j-1] is a
            # palindrome
            if (table[i + 1][j - 1] and text[i] == text[j]):
                table[i][j] = True

                if (cl > maxLength):
                    start = i
                    maxLength = cl

            i = i + 1
        cl = cl + 1
    return text[start:start + maxLength]