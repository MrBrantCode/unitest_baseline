"""
QUESTION:
Implement a function `format_phone_number(phone_number)` that formats a given US phone number according to the North American Numbering Plan (NANP). The function should accept phone numbers with non-digit characters and return a string in the canonical format "+1-XXX-XXX-XXXX". The input phone number can be a string or an integer. If the input phone number is invalid (i.e., not exactly 10 digits), return "Invalid phone number".
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