"""
QUESTION:
Create a function named `check_password_strength` that takes a password as an input and returns a boolean value indicating whether the password is strong or not. The function should check the following conditions: 
- The password length should be at least 8 characters.
- The password should contain at least one numeral.
- The password should contain at least one uppercase letter.
- The password should contain at least one lowercase letter.
- The password should contain at least one special character from the following list: !@#$%^&*()-+?_=,<>/.
If the password does not meet a condition, the function should print an error message explaining the condition. If all conditions are met, the function should print a success message and return True.
"""

def check_password_strength(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    min_password_length = 8
    if len(password) < min_password_length:
        print("Password should have at least", min_password_length, "characters")
        return False
    if not any(char.isdigit() for char in password):
        print("Password should have at least one numeral")
        return False
    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")
        return False
    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")
        return False
    if not any(char in special_characters for char in password):
        print("Password should have at least one of the symbols !@#$%^&*()-+?_=,<>/")
        return False
    else:
        print("Password is strong")
        return True