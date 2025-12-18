"""
QUESTION:
Implement a function `processFieldOfStudy` that takes a string `fieldOfStudy` as input. The function should return the input string with leading and trailing whitespace removed, converted to lowercase, and with all special characters removed except for spaces. If the input string is null, the function should return "Unknown".
"""

def processFieldOfStudy(fieldOfStudy):
    if fieldOfStudy is None:
        return "Unknown"
    else:
        processed_field = fieldOfStudy.strip().lower()
        processed_field = ''.join(e for e in processed_field if e.isalnum() or e.isspace())
        return processed_field