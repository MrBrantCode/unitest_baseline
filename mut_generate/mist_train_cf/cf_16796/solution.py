"""
QUESTION:
Create a function named extract_info that takes a string as input and returns the name, age, day of the week, and time in 24-hour format from the string. The input string is in the format "My name is [name], I am [age] years old, and today is [day of the week]. The current time is [time]." The function should use a regex pattern to extract the required information.
"""

import re

def extract_info(s):
    """
    Extract name, age, day of the week, and time in 24-hour format from a given string.

    Args:
        s (str): Input string in the format 
                 "My name is [name], I am [age] years old, and today is [day of the week]. The current time is [time]."

    Returns:
        tuple: A tuple containing the name, age, day of the week, and time in 24-hour format.
    """
    pattern = r"My name is ([A-Za-z]+), I am (\d+) years old, and today is (\w+). The current time is (\d{2}:\d{2})\."
    match = re.match(pattern, s)
    if match:
        return match.groups()
    else:
        return None