"""
QUESTION:
Create a function `validate_string(input_string)` that validates a given string. The string must contain at least 5 and at most 20 characters, including at least one number, one special character, one upper-case letter, and one lower-case letter. The function should return "String is valid" if the string meets all the conditions, otherwise, it should return an error message indicating the specific condition that is not met. The function should also handle the case where the input is not a string and return an error message.
"""

import re

def validate_string(input_string):
    if not isinstance(input_string, str):
        return "Error: Input must be a string"
    
    if len(input_string) < 5 or len(input_string) > 20:
        return "Error: String length must be between 5 and 20 characters"
    
    pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,20}$")
    
    if pattern.fullmatch(input_string):
        return "String is valid"
    else:
        return "Error: String must contain at least one upper case letter, one lower case letter, one digit and one special character"