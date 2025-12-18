"""
QUESTION:
Create a function `check_palindrome(input_string)` that determines if a given string is a palindrome, disregarding case, spaces, and punctuation. The function should return `True` if the string is a palindrome and `False` otherwise. The input string should be analyzed without any modifications, and the function should not handle any errors.
"""

def check_palindrome(input_string):
    input_string = ''.join(e for e in input_string if e.isalnum()).lower()
    return input_string == input_string[::-1]