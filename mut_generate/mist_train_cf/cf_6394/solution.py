"""
QUESTION:
Write a function named `longest_palindrome_substring` that finds the longest substring of a given length (n) that is a palindrome in a provided string. The function should return the longest palindrome substring. 

The function takes two parameters: a string (s) and an integer (n). The value of n will be 4.
"""

def longest_palindrome_substring(s, n):
    longest_palindrome = ""
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring == substring[::-1] and len(substring) > len(longest_palindrome):
            longest_palindrome = substring
    return longest_palindrome