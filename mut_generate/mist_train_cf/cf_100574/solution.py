"""
QUESTION:
Write a function named `extract_device_name` that takes a string `text` as input and returns the device name if a string that starts with "Name: " is found, otherwise returns "Device name not found". The function should use regular expression to search for the pattern and handle the case where the pattern is not found.
"""

import re

def extract_device_name(text):
    """
    Extracts the device name from a given text if a string that starts with "Name: " is found.

    Args:
        text (str): The input text to search for the device name.

    Returns:
        str: The device name if found, otherwise "Device name not found".
    """
    match = re.search(r"Name: (.*)", text)
    if match:
        return match.group(1)
    else:
        return "Device name not found"