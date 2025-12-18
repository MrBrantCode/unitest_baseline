"""
QUESTION:
Create a function named `longest_palindrome` that takes a non-empty string as input and returns the longest palindromic substring. The input string only contains characters (no spaces or special characters) and the function should return the longest contiguous substring that is a palindrome. The function should be efficient enough to handle long strings.
"""

def longest_palindrome(s):
    n = len(s)
    
    # table to store whether a substring is palindrome or not
    table = [[False]*n for _ in range(n)]
    
    # all substrings of length 1 are palindromes
    for i in range(n):
        table[i][i] = True
    
    max_len = 1
    start = 0
    # check for substring of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start = i
            max_len = 2
            
    # check for substrings of length 3 and more
    for l in range(3, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j] and table[i+1][j-1]:
                table[i][j] = True
                if l > max_len:
                    start = i
                    max_len = l

    return s[start:start+max_len]