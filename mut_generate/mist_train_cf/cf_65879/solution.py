"""
QUESTION:
Create a `register_user` function that takes four parameters: `real_name`, `email`, `password`, and `location`. This function should register a new user into a data structure called 'users' and perform the following checks: 
- The password must be at least 8 characters long, containing at least one uppercase letter, one lowercase letter, and one digit.
- The location must not be in a list of prohibited zones.

If the password or location is invalid, return a corresponding error message. Otherwise, create a new user with the given information and add it to the 'users' data structure, returning a success message.
"""

import re

#replace with actual prohibited zones
prohibited_zones = ['prohibited_zone1', 'prohibited_zone2', 'prohibited_zone3']

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    return True

def check_location(location):
    if location in prohibited_zones:
       return False
    return True

def register_user(real_name, email, password, location):
    if not check_password_strength(password):
        return "Registration Failed: Your password is too weak."
    if not check_location(location):
        return "Registration Failed: Your location is in a prohibited zone."
    return "Registration Successful."