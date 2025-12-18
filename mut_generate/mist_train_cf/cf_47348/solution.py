"""
QUESTION:
Create a function `extract_info` that takes a string `text` as input, extracts the individual's name and the day of the week, and returns a tuple containing the extracted name and day. The input string is expected to be in the format "My name is [name], and today is [day]" where [name] is the individual's name and [day] is the day of the week.
"""

import re

def extract_info(text):
    name_pattern = r"My name is (\w+)"
    name_match = re.search(name_pattern, text)
    name = name_match.group(1) if name_match else None

    day_pattern = r"today is (\w+)"
    day_match = re.search(day_pattern, text)
    day = day_match.group(1) if day_match else None
    
    return (name, day)