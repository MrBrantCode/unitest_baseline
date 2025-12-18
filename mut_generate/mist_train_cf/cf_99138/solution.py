"""
QUESTION:
Create a function called `filter_and_extract_last_five` that takes a list of strings as input, filters out any values that contain letters or special characters, and extracts the last 5 characters from the remaining values. The function should only return the extracted values that are numeric and have at least 5 characters.
"""

import re

def filter_and_extract_last_five(data):
    result = []
    for value in data:
        # use regular expressions to check for non-numeric characters
        if re.search('[^0-9]', value) is None and len(value) >= 5:
            # if the value contains only numeric characters, extract the last 5 characters
            result.append(value[-5:])
    return result