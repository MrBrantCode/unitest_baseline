"""
QUESTION:
Create a function `check_string(my_string)` that takes a string `my_string` as input and returns whether it meets the following conditions: 
- ends with a combination "py" that is not nested within brackets of any kind
- the "py" combination is preceded by a consonant
- the "py" combination is succeeded by a number
- the "py" combination is at the end of the string
"""

import re

def check_string(my_string):
    # Regular expression pattern
    pattern = r"(?!\[\w*py\])[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]py\d$"
    return bool(re.search(pattern, my_string))