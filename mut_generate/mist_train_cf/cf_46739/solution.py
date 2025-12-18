"""
QUESTION:
Write a function `check_palindrome_substrings(s, n)` that takes a string `s` and an integer `n` as inputs, and checks if each of the 'n' sized consecutive substrings is a palindrome or not. Return a list of Boolean values for each substring. If 'n' exceeds the length of the string, return "Invalid Input". The input string will contain only lowercase English letters and the length of the input string and the value of 'n' will be between 1 and 10^3.
"""

def check_palindrome_substrings(s, n):
    if n > len(s):
        return "Invalid Input"
    else:
        return [s[i:i+n] == s[i:i+n][::-1] for i in range(len(s) - n + 1)]