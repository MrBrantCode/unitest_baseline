"""
QUESTION:
Create a function called `is_palindrome(str)` that determines whether a given input string is the same forwards and backwards. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def entrance(str):
    reversedStr = str[::-1]
    return reversedStr == str