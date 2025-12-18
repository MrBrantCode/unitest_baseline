"""
QUESTION:
Write a function named `check_string` that takes a string as input and returns `True` if the string only contains alphabets and has at least one uppercase letter and one lowercase letter, and `False` otherwise. The function should not use any external libraries or modules.
"""

def check_string(string):
    # Check if the string only contains alphabets
    if not string.isalpha():
        return False
    
    # Check if the string contains at least one uppercase and one lowercase letter
    if not any(char.isupper() for char in string) or not any(char.islower() for char in string):
        return False
    
    return True