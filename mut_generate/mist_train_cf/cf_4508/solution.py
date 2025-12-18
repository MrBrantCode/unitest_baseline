"""
QUESTION:
Write a regular expression to match a string of consecutive numbers in the format "ABC-DEF-GHIJ" where ABC, DEF, and GHIJ are three consecutive numbers with a minimum of 3 digits each. The string should not contain any whitespace characters and should be enclosed within double quotes. The regular expression should match the entire string from start to end.
"""

import re

def entrance(s):
    pattern = r'^"[0-9]{3}-[0-9]{3}-[0-9]{4}"$'
    return bool(re.match(pattern, s))