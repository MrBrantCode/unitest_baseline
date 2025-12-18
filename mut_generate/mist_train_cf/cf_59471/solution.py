"""
QUESTION:
Create a function `is_palindrome` that determines whether a given string is a palindrome, ignoring case sensitivity. The function should take a string as input and return `True` if the string is a palindrome and `False` otherwise.
"""

def entrance(string):
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False