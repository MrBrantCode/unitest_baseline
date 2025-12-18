"""
QUESTION:
Design a function named `check_string` that takes an input string and checks if it contains the terms "hello" and "world" between two to three times each, ignoring any special characters and numerics, and without considering substrings or parts of other words.
"""

import re

def check_string(input_string):
    # Checking for "hello"
    hello_pattern = r'\bhello\b'
    hello_matches = re.findall(hello_pattern, input_string)
    if len(hello_matches) < 2 or len(hello_matches) > 3:
        return False

    # Checking for "world"
    world_pattern = r'\bworld\b'
    world_matches = re.findall(world_pattern, input_string)
    if len(world_matches) < 2 or len(world_matches) > 3:
        return False

    return True