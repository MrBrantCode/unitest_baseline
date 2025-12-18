"""
QUESTION:
Write a function `is_palindrome` that determines whether a given string is a palindrome using a stack data structure. The function should ignore case and special characters, and only consider alphanumeric characters. It should not use any built-in functions or libraries for string manipulation.
"""

def is_palindrome(string):
    clean_string = ""
    for char in string:
        if char.isalnum():
            clean_string += char
    clean_string = clean_string.lower()
    stack = []
    for char in clean_string:
        stack.append(char)
    for char in clean_string:
        if stack.pop() != char:
            return False
    return True