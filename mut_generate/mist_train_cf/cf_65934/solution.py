"""
QUESTION:
Write a function `validate_string(input_string)` that checks if a given string meets the following conditions:
- The string length is between 5 and 15 characters (inclusive).
- The string only contains alphanumeric characters (no special characters or spaces).
- The string contains at least one uppercase letter.
Return an error message if any condition is not met; otherwise, return 'Valid input'.
"""

def validate_string(input_string):
    a = 5
    b = 15

    if len(input_string) < a or len(input_string) > b:
        return 'Invalid input: String length must be between 5 and 15 characters'
    
    if not input_string.isalnum():
        return 'Invalid input: String must only contain alphanumeric characters'

    if not any(char.isupper() for char in input_string):
        return 'Invalid input: String must contain at least one uppercase letter'
    
    return 'Valid input'