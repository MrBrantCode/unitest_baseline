"""
QUESTION:
Find the longest palindromic substring in a given string. A palindromic substring is a substring that remains the same when its characters are reversed. The function should take a string as input and return the longest palindromic substring as a string. The function name should be `longest_palindromic_substring`. There are no specific restrictions on the input string.
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