"""
QUESTION:
Create a function `string_validator(s)` that takes a single string `s` as input and returns a boolean value. The input string should meet the following requirements: 
- have a minimum length of 8 and a maximum length of 12 characters,
- contain at least 2 digits, 
- include at least 2 upper-case letters, 
- if it includes any special characters, they must only be from the set (!, ?, _, @).
If the string fails any of the requirements, the function should identify which requirement(s) the string failed.
"""

def string_validator(s):
    count_upper = sum(1 for c in s if c.isupper())
    count_digits = sum(1 for c in s if c.isdigit())
    special_chars = "!?_@"
    errors = []
    if not 8 <= len(s) <= 12:
        errors.append("Length should be between 8 and 12 characters")
    if count_upper < 2:
        errors.append("Should contain at least 2 upper-case letters")
    if count_digits < 2:
        errors.append("Should contain at least 2 digits")
    if not all(c in special_chars for c in s if not c.isalnum()):
        errors.append("Only special characters allowed are !, ?, _, @")
    
    if not errors: 
        return True
    else: 
        print(f"Failure for string '{s}': {', '.join(errors)}")
        return False