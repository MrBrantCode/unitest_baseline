"""
QUESTION:
Create a function named `format_phone_number` that takes a phone number as input, removes any non-digit characters, and returns a string representing the phone number in the format "+1-XXX-XXX-XXXX". The function should be able to handle phone numbers passed as strings or integers and may contain additional characters such as spaces or parentheses.
"""

def format_phone_number(phone_number):
    # Remove any non-digit characters from the input
    phone_number = ''.join(filter(str.isdigit, str(phone_number)))
    
    # Add the country code and hyphens to the phone number
    formatted_number = "+1-" + phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]
    
    return formatted_number