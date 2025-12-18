"""
QUESTION:
Implement a function named `is_club_guid` that takes an input string and returns True if it is a valid GUID (Globally Unique Identifier) in the format "8-4-4-4-12" (a 32-character hexadecimal string with hyphens), and False otherwise. The GUID should only contain hexadecimal digits (0-9, a-f, A-F).
"""

import re

def is_club_guid(input_string):
    # Define the pattern for a valid GUID
    guid_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    
    # Check if the input string matches the GUID pattern
    return bool(re.match(guid_pattern, input_string))