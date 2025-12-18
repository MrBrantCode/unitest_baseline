"""
QUESTION:
Create a function `password_check(password)` that checks the validity of a given password. The password is valid if it meets the following criteria: 
- At least 8 characters long
- Contains at least one lowercase letter
- Contains at least one uppercase letter
- Contains at least one numeral
- Contains at least one of the symbols $@_
- Does not contain any space. 
The function should return `True` if the password is valid and `False` otherwise, and print the reason for invalidity.
"""

import re

def password_check(password):
    # Checking for the criteria of password
    if len(password)<8:
        print("Password should be at least 8 characters long")
        return False
    elif not re.search("[a-z]", password):
        print("Password should have at least one lowercase letter")
        return False
    elif not re.search("[A-Z]", password):
        print("Password should have at least one uppercase letter")
        return False
    elif not re.search("[0-9]", password):
        print("Password should have at least one numeral")
        return False
    elif not re.search("[_@$]", password):
        print("Password should have at least one of the symbols $@_")
        return False
    elif re.search("\s", password):
        print("Password should not have any space")
        return False
    else:
        print("Valid Password")
        return True