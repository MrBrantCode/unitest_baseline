"""
QUESTION:
Write a function `longest_palindrome_substring` that takes a string `string` as input and returns the longest palindromic substring. A palindromic substring reads the same backward as forward. The function should find the longest substring that meets this condition and return it as a string.
"""

def longest_palindrome_substring(string):
    n = len(string)
    t = [[False for _ in range(n)] for _ in range(n)]  
    max_length = 1
    i = 0
    while (i < n): 
        t[i][i] = True
        i = i + 1
    start = 0
    i = 0
    while i < n - 1: 
        if (string[i] == string[i + 1]): 
            t[i][i + 1] = True
            start = i 
            max_length = 2
        i = i + 1
    k = 3
    while k <= n: 
        i = 0
        while i < (n - k + 1): 
            j = i + k - 1
            if (t[i + 1][j - 1] and 
                    string[i] == string[j]): 
                t[i][j] = True
                if (k > max_length): 
                    start = i 
                    max_length = k 
            i = i + 1
        k = k + 1
    longest_palindrome = string[start:start+max_length]
    return longest_palindrome