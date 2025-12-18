"""
QUESTION:
Create a function called `unicode_to_upper` that takes a string as input and returns the string with all characters converted to uppercase. The function should correctly handle both English and non-English characters, and it must not use the built-in "upper" method.
"""

import unicodedata

def unicode_to_upper(input_string):
    return ''.join(
        (unicodedata.normalize('NFKD', char)[0].upper() 
         if unicodedata.combining(char) == 0 else char) 
        for char in input_string
    )