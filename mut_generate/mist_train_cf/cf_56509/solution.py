"""
QUESTION:
Create a function `substitute_numeral(text)` that takes a string as input and returns a new string where every digit is replaced with the hashtag symbol (#).
"""

import re 

def substitute_numeral(text):
    return re.sub(r'\d', '#', text)