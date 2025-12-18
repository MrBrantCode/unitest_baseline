"""
QUESTION:
Create a function named `parse_details` that takes a string `s` as input. The function should return a list of words divided by either a comma or a colon. If neither a comma nor a colon is present in the string, the function should return the count of lower-case alphabetic characters with odd ASCII values in the string.
"""

def parse_details(s):
    if ',' in s:
        return s.split(',')
    elif ':' in s:
        return s.split(':')
    else:
        return len([i for i in s if i.islower() and ord(i) % 2 == 1])