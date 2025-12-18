"""
QUESTION:
Write a function `validate_string(string)` that checks if a given string only contains alphabets and at least one uppercase letter, one lowercase letter, one special character, and one digit. The function should return `True` if all conditions are met and `False` otherwise.
"""

import re

def validate_string(string):
    if not string.isalpha():
        print("String should only contain alphabets.")
        return False
    
    if not any(char.isupper() for char in string):
        print("String should contain at least one uppercase letter.")
        return False
    
    if not any(char.islower() for char in string):
        print("String should contain at least one lowercase letter.")
        return False
    
    if not re.search("[!@#$%^&*(),.?\":{}|<>0-9]", string):
        print("String should contain at least one special character and one digit.")
        return False
    
    return True