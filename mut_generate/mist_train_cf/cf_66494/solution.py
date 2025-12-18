"""
QUESTION:
Create a function called `match_hello_world` that uses regular expression to identify if the string "Hello World!" is present in a given text. The function should return "Match found" if the string is found, otherwise it should return "Match not found". The function should consider "Hello World!" as a fixed string and not as a pattern. It should also handle special characters in the string "Hello World!" if any.
"""

import re

def match_hello_world(text):
    pattern = r'Hello World!'
    match = re.search(pattern, text)
    
    if match:
        return "Match found"
    else:
        return "Match not found"