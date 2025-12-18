"""
QUESTION:
Write a function called `parse_string` that takes a string as input. The string contains information about multiple people separated by the word "person". Each person's information is in the format "name" followed by their name, "age" followed by their age, and "occupation" followed by their occupation. Return a dictionary where the keys are the names of the people and the values are dictionaries containing the person's age and occupation.
"""

import re

def parse_string(s):
    result = {}
    pattern = r"name (\w+) age (\d+) occupation (\w+)"
    matches = re.finditer(pattern, s)
    
    for match in matches:
        name = match.group(1)
        age = int(match.group(2))
        occupation = match.group(3)
        
        result[name] = {"age": age, "occupation": occupation}
    
    return result