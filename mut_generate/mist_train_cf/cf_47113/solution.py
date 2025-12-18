"""
QUESTION:
Write a function `find_palindromic_substrings(input_string)` that takes a string `input_string` of length N as input and returns all existing substrings that read the same backward as forward. The function should consider every possible substring of the input string.
"""

def find_palindromic_substrings(input_string):
    N = len(input_string)
    palindromic_substrings = []
    for i in range(N):
        for j in range(i, N):
            substring = input_string[i:j+1]
            if substring == substring[::-1]: 
                palindromic_substrings.append(substring)
    return palindromic_substrings