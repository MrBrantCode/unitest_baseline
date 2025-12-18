"""
QUESTION:
Create a function `extract_info` that takes a string `text` as input and returns a tuple containing the name, age, and day of the week. The input string is expected to be in the format "My name is [name], I am [age] years old, and today is [day of the week]". The function should use regular expressions to extract the required information.
"""

import re

def extract_info(text):
    pattern = r"My name is (\w+), I am (\d+) years old, and today is (\w+)"
    matches = re.search(pattern, text)
    
    if matches:
        return (matches.group(1), matches.group(2), matches.group(3))
    else:
        return None