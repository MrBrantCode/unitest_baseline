"""
QUESTION:
Write a function `extract_device_name` that takes a string `text` as input and returns the device name if a string that starts with "Name: " is found, otherwise return "Device name not found".
"""

import re

def extract_device_name(text):
    match = re.search(r"Name: (.*)", text)
    if match:
        return match.group(1)
    else:
        return "Device name not found"