"""
QUESTION:
Congratulations! That Special Someone has given you their phone number.

But WAIT, is it a valid number? 

Your task is to write a function that verifies whether a given string contains a valid British mobile (cell) phone number or not. 

If valid, return 'In with a chance'.

If invalid, or if you're given an empty string, return 'Plenty more fish in the sea'.

A number can be valid in the following ways: 

Here in the UK mobile numbers begin with '07' followed by 9 other digits, e.g. '07454876120'.

Sometimes the number is preceded by the country code, the prefix '+44', which replaces the '0' in ‘07’, e.g. '+447454876120'.

And sometimes you will find numbers with dashes in-between digits or on either side, e.g. '+44--745---487-6120' or '-074-54-87-61-20-'. As you can see, dashes may be consecutive. 

Good Luck Romeo/Juliette!
"""

import re

def validate_phone_number(phone_number: str) -> str:
    # Define the return messages
    valid_message = 'In with a chance'
    invalid_message = 'Plenty more fish in the sea'
    
    # Check if the input string is empty
    if not phone_number:
        return invalid_message
    
    # Remove all dashes from the phone number
    cleaned_number = re.sub('-', '', phone_number)
    
    # Define the regex pattern for a valid UK mobile number
    pattern = '^(\\+44|0)7\\d{9}$'
    
    # Check if the cleaned number matches the pattern
    if re.match(pattern, cleaned_number):
        return valid_message
    else:
        return invalid_message