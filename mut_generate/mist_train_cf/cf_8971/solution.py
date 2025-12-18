"""
QUESTION:
Write a function called `is_palindrome` that checks if a given string is a palindrome without using built-in string reversal functions or data structures, such as slicing or the `reverse()` function.
"""

def entance(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True