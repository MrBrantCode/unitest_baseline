"""
QUESTION:
Create a function `is_palindrome` that determines if a given sequence of characters is a palindrome. The function should not use any built-in functions to reverse the string or check for palindromes. It should return `True` if the input string is a palindrome and `False` otherwise. The function should only consider the input string itself and not any additional parameters.
"""

def is_palindrome(s):
    length = len(s)
    for i in range(0, length):
        if s[i] != s[length-i-1]:
            return False
    return True