"""
QUESTION:
Create a function `check_zip_code(zip_code)` that validates a United States postal zip code. The function should return `True` if the zip code is valid and `False` otherwise. A valid zip code is either five digits or five digits followed by a hyphen and four more digits (zip+4 code).
"""

import re

def check_zip_code(zip_code):
    # Defining pattern to capture 5 digits or 5-4 digits separated by a hyphen
    pattern = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")

    # Checking if the pattern matches
    return bool(pattern.match(zip_code))