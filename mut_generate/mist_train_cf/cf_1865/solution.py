"""
QUESTION:
Write a function `extract_info` that takes a string `text` as input, extracts the name, age, day of the week, time in 24-hour format, and location from each statement in the text, and returns a list of tuples containing the extracted information. 

The input string may contain multiple statements, each in the format "My name is [name], I am [age] years old, and today is [day of the week]. The current time is [time]. This statement is being made in [location]."

The extracted information should be returned as a list of tuples, where each tuple contains the name (string), age (integer), day of the week (string), time (string), and location (string).
"""

import re

def extract_info(text):
    """
    Extracts the name, age, day of the week, time in 24-hour format, and location 
    from each statement in the text and returns a list of tuples containing the 
    extracted information.

    Args:
        text (str): The input string containing one or more statements.

    Returns:
        list[tuple]: A list of tuples, where each tuple contains the name (string), 
        age (integer), day of the week (string), time (string), and location (string).
    """
    pattern = r"My name is (\w+), I am (\d+) years old, and today is (\w+). The current time is (\d{2}:\d{2}). This statement is being made in (\w+)."
    matches = re.findall(pattern, text)
    return [(match[0], int(match[1]), match[2], match[3], match[4]) for match in matches]