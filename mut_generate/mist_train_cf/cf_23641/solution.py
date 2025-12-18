"""
QUESTION:
Create a function called 'is_palindrome' that takes a string as input and returns a boolean indicating whether the string is a palindrome, i.e., it reads the same backward as forward.
"""

def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True