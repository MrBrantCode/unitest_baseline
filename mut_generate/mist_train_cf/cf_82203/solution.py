"""
QUESTION:
Write a function called `validate_string` that takes a character sequence as input and returns a boolean value and a corresponding error message. The function should validate the input sequence based on the following conditions:

- The sequence must be between 5 and 20 characters in length.
- The sequence must not start with a numeric value.
- The sequence must not include any special characters except underscore (_).
- At least one letter in the sequence must be capitalized.
- The sequence must include at least one numeric value.

Return `True` and a success message if all conditions are met; otherwise, return `False` and the corresponding error message.
"""

import re

def validate_string(seq):
    # Check length of character sequence
    if len(seq) < 5 or len(seq) > 20:
        return False, 'Error: The sequence must be between 5 and 20 characters in length.'
    
    # Check if sequence starts with a numeral
    if seq[0].isdigit():
        return False, 'Error: The sequence cannot start with a numeric value.'
    
    # Check for presence of special characters except underscore
    if not re.match('^[a-zA-Z0-9_]*$', seq):
        return False, 'Error: The sequence should not include any special characters except underscore (_).'
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in seq):
        return False, 'Error: At least one letter in the sequence must be capitalized.'
    
    # Check for presence of numeric value
    if not any(char.isdigit() for char in seq):
        return False, 'Error: The sequence must include at least one numeric value.'
    
    # If all checks are passed, return True
    return True, 'Success: The sequence is valid.'