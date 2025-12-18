"""
QUESTION:
Write a function called `check_strings` that takes an array of strings as input and returns a boolean value. The function should return `True` if every string in the array contains at least one digit and one uppercase letter. Otherwise, it should return `False`.
"""

def check_strings(arr):
    for string in arr:
        has_digit = False
        has_uppercase = False
        
        for char in string:
            if char.isdigit():
                has_digit = True
            elif char.isupper():
                has_uppercase = True
                
            if has_digit and has_uppercase:
                break
        
        if not (has_digit and has_uppercase):
            return False
    
    return True