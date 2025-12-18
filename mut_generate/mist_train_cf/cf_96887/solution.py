"""
QUESTION:
Create a function called `check_string` that takes one argument, a string. The function should return `True` if the string contains only alphabetical characters, has a length of at least 5 characters, contains at least one uppercase letter, one lowercase letter, and one digit, otherwise return `False`.
"""

def check_string(string):
    # Check if string contains only alphabetical characters and has a length of at least 5
    if not string.isalpha() or len(string) < 5:
        return False
    
    # Check if string contains at least one uppercase letter, one lowercase letter, and one digit
    if not any(char.isupper() for char in string):
        return False
    if not any(char.islower() for char in string):
        return False
    if not any(char.isdigit() for char in string):
        return False
    
    return True