"""
QUESTION:
Create a regular expression to match numbers in the format 1xx-xxx-xxxx where the two digits following '1' must be between 0 and 50.
"""

def entrance(number):
    import re
    pattern = r'\b1[0-4][0-9]-\d{3}-\d{4}\b'
    return bool(re.fullmatch(pattern, number))