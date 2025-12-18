"""
QUESTION:
Given a string, implement a function `longest_palindromic_substring(string)` that returns the longest palindromic substring within the string. A palindromic substring is a substring that remains the same when its characters are reversed. The function should have a time complexity of O(n^2), where n is the length of the input string, and should use dynamic programming to solve the problem.
"""

def longest_palindromic_substring(string):
    n = len(string)
    table = [[False] * n for _ in range(n)]
    start_index = 0
    max_length = 1
    
    # Initialize diagonal cells as True
    for i in range(n):
        table[i][i] = True
    
    # Check for palindromic substrings of length 2
    for i in range(n-1):
        if string[i] == string[i+1]:
            table[i][i+1] = True
            start_index = i
            max_length = 2
    
    # Check for palindromic substrings of length > 2
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if string[i] == string[j] and table[i+1][j-1]:
                table[i][j] = True
                start_index = i
                max_length = length
    
    return string[start_index:start_index + max_length]