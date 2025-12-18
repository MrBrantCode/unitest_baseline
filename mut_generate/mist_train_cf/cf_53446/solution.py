"""
QUESTION:
Create a function `match_string` that takes a string as input and returns True if the string contains a date in the format 'dd-mm-yyyy' anywhere in the string and ends with the word 'Goodbye', otherwise return False.
"""

import re

def match_string(string):
    pattern = r'\b(3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-(?:[0-9]{2})?[0-9]{2}\b.*Goodbye$'
    return bool(re.search(pattern, string))