"""
QUESTION:
Write a function `longest_palindrome` that takes a string as input and returns the longest palindromic substring. The function should use dynamic programming to efficiently find the longest palindrome. The input string can contain any characters, and the function should return a single substring (even if there are multiple palindromes of the same maximum length).
"""

def longest_palindrome(string):
    n = len(string)
    table = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    for i in range(n):
        table[i][i] = True

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if string[i] == string[j] and (j-i == 1 or table[i+1][j-1]):
                table[i][j] = True
                if j-i+1 > max_length:
                    start = i
                    max_length = j-i+1

    return string[start:start+max_length]