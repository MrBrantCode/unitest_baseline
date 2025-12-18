"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string is the same when its characters are reversed. The function should return `True` if the string is a palindrome and `False` otherwise. The input string will only contain lowercase English letters.
"""

def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n-i-1]:
            return False
    return True