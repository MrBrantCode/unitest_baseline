"""
QUESTION:
Write a function `extract_info` that takes a string as input and returns the name, age, and day of the week. The input string is in the format "My name is [name], I am [age] years old, and today is [day of the week]". The function should use a regex pattern to extract the required information.
"""

import re

def extract_info(text):
    """
    Extracts the name, age, and day of the week from a given string.

    Args:
    text (str): The input string in the format "My name is [name], I am [age] years old, and today is [day of the week]".

    Returns:
    dict: A dictionary containing the extracted name, age, and day of the week.
    """
    
    pattern = r"My name is (\w+), I am (\d+) years old, and today is (\w+)"
    matches = re.search(pattern, text)
    
    if matches:
        name = matches.group(1)
        age = matches.group(2)
        day_of_week = matches.group(3)
        
        return {
            "Name": name,
            "Age": age,
            "Day of the Week": day_of_week
        }
    else:
        return None