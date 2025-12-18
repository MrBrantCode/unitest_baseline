"""
QUESTION:
Write a function named `is_palindrome_list` that takes a list of strings as input and returns `True` if all strings in the list are palindromes, and `False` otherwise.
"""

def is_palindrome_list(string_list):
    for string in string_list:
        if string != string[::-1]:  # Check if the string is not equal to its reverse
            return False
    return True