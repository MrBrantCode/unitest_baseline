"""
QUESTION:
Create a function named `match_strings` that takes two parameters: `first_string` and `second_string`. The function should return `True` if the following conditions are met: `first_string` is a combination of lowercase and uppercase letters, `second_string` is a combination of lowercase letters, uppercase letters, digits, and special characters, `second_string` is a palindrome, and `second_string` contains at least one digit. Otherwise, the function should return `False`.
"""

import re

def match_strings(first_string, second_string):
    # Check if first string is a combination of lowercase and uppercase letters
    if not re.match("^[a-zA-Z]+$", first_string):
        return False
    
    # Check if second string is a combination of lowercase letters, uppercase letters, digits, and special characters
    if not re.match("^[a-zA-Z0-9!@#$%^&*()_+{}|:\"<>?~`-]+$", second_string):
        return False
    
    # Check if second string is a palindrome
    if second_string != second_string[::-1]:
        return False
    
    # Check if second string contains at least one digit
    if not re.search("[0-9]", second_string):
        return False
    
    return True