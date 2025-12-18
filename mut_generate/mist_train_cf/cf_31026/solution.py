"""
QUESTION:
Write a function called `extract_entry_points` that takes a string `entry_points` as input, where the string is formatted as a series of sections enclosed in square brackets, each containing one or more key-value pairs separated by an equal sign. The function should return a dictionary where the keys are the section names and the values are dictionaries containing the key-value pairs for each entry point within that section. The input string may contain multiple sections and entry points, and the section and key names may contain any characters except square brackets and equals signs. The function should ignore any blank lines or lines that do not match the expected format.
"""

import re

def extract_entry_points(entry_points: str) -> dict:
    entry_points_dict = {}
    current_section = None
    for line in entry_points.splitlines():
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            entry_points_dict[current_section] = {}
        elif '=' in line and current_section:
            key, value = map(str.strip, line.split('='))
            entry_points_dict[current_section][key] = value
    return entry_points_dict