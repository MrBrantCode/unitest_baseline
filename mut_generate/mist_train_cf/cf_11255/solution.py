"""
QUESTION:
Write a function `findPalindromes(s)` that identifies all unique palindromic substrings in a given string `s` with a time complexity of O(n), where n is the length of the string. The function should return a list of all unique palindromic substrings found in the string.
"""

def findPalindromes(s):
    palindromes = set()
    n = len(s)
    # initialize a 2D boolean array to store the palindrome information
    isPalindrome = [[False for _ in range(n)] for _ in range(n)]

    # all individual characters are palindromes
    for i in range(n):
        isPalindrome[i][i] = True
        palindromes.add(s[i])

    # check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            isPalindrome[i][i + 1] = True
            palindromes.add(s[i:i + 2])

    # check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and isPalindrome[i + 1][j - 1]:
                isPalindrome[i][j] = True
                palindromes.add(s[i:j + 1])

    return list(palindromes)