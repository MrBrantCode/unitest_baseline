"""
QUESTION:
Create a function called `longest_palindrome_subseq` that takes a string `s` as input and returns the length of the longest palindromic subsequence within `s`. The input string can be empty and the function should handle this case.
"""

def longest_palindrome_subseq(s):
    if len(s) == 0:
        return 0

    n = len(s)
    table = [[0]*n for _ in range(n)]

    for i in range(n):
        table[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = 2
        else:
            table[i][i+1] = 1

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            
            if s[i]==s[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])

    return table[0][n-1]