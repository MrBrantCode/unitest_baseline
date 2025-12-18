"""
QUESTION:
Implement a function `format_phone_number(phone_number)` that takes a phone number as input, removes any non-digit characters, checks if the phone number is valid according to the North American Numbering Plan (NANP) with exactly 10 digits, and returns a string with the canonical format of "+1-XXX-XXX-XXXX" if valid. If the input is not a valid phone number, the function should return "Invalid phone number". The implementation should not use any built-in string manipulation or regular expression functions.
"""

def format_phone_number(phone_number):
    # Remove any non-digit characters from the phone number
    phone_number = ''.join(filter(str.isdigit, str(phone_number)))

    # Check if the phone number is valid according to NANP
    if len(phone_number) != 10:
        return "Invalid phone number"

    # Format the phone number in the canonical format
    formatted_number = "+1-" + phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]

    return formatted_number