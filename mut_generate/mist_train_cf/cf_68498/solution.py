"""
QUESTION:
Create a function `verify_password(password)` that checks if a given password is valid. The password is valid if it meets the following conditions: 
- It is at least 8 characters long.
- It contains at least one digit.
- It contains at least one uppercase letter.
- It contains at least one lowercase letter.
- It does not contain any spaces.
- It contains at least one of the special characters $, @, #, or %. 
The function should return a string indicating whether the password is valid or not, along with a specific reason if it is not.
"""

def verify_password(password):
    if len(password) < 8:
        return "Invalid: Password should be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "Invalid: Password should have at least one numeral"
    if not any(char.isupper() for char in password):
        return "Invalid: Password should have at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Invalid: Password should have at least one lowercase letter"
    if " " in password:
        return "Invalid: Password should not have any space"
    special_characters = ["$", "@", "#", "%", "&"]
    if not any(char in special_characters for char in password):
        return "Invalid: Password should have at least one of the symbols $@#%"
    return "Valid password"