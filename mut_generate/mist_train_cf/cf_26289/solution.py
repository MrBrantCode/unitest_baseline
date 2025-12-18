"""
QUESTION:
Write a function named `is_palindrome` that takes a string `str` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should be case-insensitive, meaning it should treat uppercase and lowercase letters as the same.
"""

def is_palindrome(str): 
    # First convert all to the same case
    str = str.lower()
    return str == str[::-1]