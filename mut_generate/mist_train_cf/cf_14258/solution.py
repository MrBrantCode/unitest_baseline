"""
QUESTION:
Write a function `check_substring(strings, substring)` that checks if a given substring is present in a set of strings and is a palindrome. The function should return `True` if the substring is present and is a palindrome, and `False` otherwise.
"""

def check_substring(strings, substring):
    for string in strings:
        if substring in string and substring == substring[::-1]:
            return True
    return False