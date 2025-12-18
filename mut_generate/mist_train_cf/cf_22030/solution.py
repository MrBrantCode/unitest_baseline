"""
QUESTION:
Create a function `check_string` that takes a string as input and returns `True` if the string meets the following conditions:
- The string contains only alphabetical characters.
- The length of the string is at least 5 characters.
- The string contains at least one uppercase letter, one lowercase letter, and one digit.
Return `False` otherwise.
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