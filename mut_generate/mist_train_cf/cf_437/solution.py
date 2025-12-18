"""
QUESTION:
Create a function `is_palindrome_list(lst)` that takes a list of strings `lst` as input and returns `True` if all strings in the list are palindromes (ignoring special characters, spaces, and case) and `False` otherwise.
"""

def is_palindrome_list(lst):
    for string in lst:
        modified_string = ""
        for char in string:
            if char.isalnum():
                modified_string += char.lower()
        if modified_string != modified_string[::-1]:
            return False
    return True