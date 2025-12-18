"""
QUESTION:
Write a function named `get_first_and_middle_names` that takes a string `full_name` as input and returns a tuple containing the first name and middle name(s) of a user. The full name may contain one or more middle names, or no middle names at all, and is assumed to be in the format "First name Middle name(s) Last name".
"""

import re

def get_first_and_middle_names(full_name):
    # dividing the name into words
    parts = full_name.split()

    if len(parts) == 1:
        return parts[0], None   # only first name is present
    elif len(parts) == 2:
        return parts[0], None   # No Middle name present
    else:
        # return first and all middle names
        return parts[0], ' '.join(parts[1:-1])