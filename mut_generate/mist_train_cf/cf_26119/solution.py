"""
QUESTION:
Create a regular expression pattern to match valid phone numbers in a given string. The valid phone number format is XXX-XXX-XXXX, where X represents a digit. The function should match one or more occurrences of this pattern in the string.
"""

def phone_number_match(s):
    regex_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return regex_pattern