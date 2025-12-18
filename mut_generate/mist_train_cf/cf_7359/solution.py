"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if it is a palindrome (ignoring non-alphanumeric characters and case differences) and `False` otherwise, without using any built-in string manipulation or regular expression functions.
"""

def is_palindrome(string):
    alphanumeric_string = ''.join(char.lower() for char in string if char.isalnum())
    left, right = 0, len(alphanumeric_string) - 1
    while left < right:
        if alphanumeric_string[left] != alphanumeric_string[right]:
            return False
        left += 1
        right -= 1
    return True