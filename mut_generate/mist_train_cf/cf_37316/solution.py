"""
QUESTION:
Create a function `convert_to_numeric(phone_number)` that takes a string `phone_number` containing alphanumeric characters and dashes as input and returns the converted numeric format of the phone number, where alphabetic characters are replaced with their corresponding numeric representation based on a standard phone keypad and non-alphanumeric characters are preserved.
"""

def convert_to_numeric(phone_number):
    numeric_phone = ''
    for ch in phone_number:
        if ch.islower():
            ch = ch.upper()
        if ch.isdigit():
            numeric_phone += ch
        elif ch == '-':
            numeric_phone += '-'
        elif ch in ['A', 'B', 'C']:
            numeric_phone += '2'
        elif ch in ['D', 'E', 'F']:
            numeric_phone += '3'
        elif ch in ['G', 'H', 'I']:
            numeric_phone += '4'
        elif ch in ['J', 'K', 'L']:
            numeric_phone += '5'
        elif ch in ['M', 'N', 'O']:
            numeric_phone += '6'
        elif ch in ['P', 'Q', 'R', 'S']:
            numeric_phone += '7'
        elif ch in ['T', 'U', 'V']:
            numeric_phone += '8'
        elif ch in ['W', 'X', 'Y', 'Z']:
            numeric_phone += '9'
    return numeric_phone