"""
QUESTION:
Write a function `is_palindrome(string)` that determines whether a given string is a palindrome using a stack data structure, ignoring case sensitivity. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(string):
    string = string.lower()
    stack = []
    
    for char in string:
        stack.append(char)
    
    reversed_string = ""
    
    while len(stack) > 0:
        reversed_string += stack.pop()
    
    return string == reversed_string