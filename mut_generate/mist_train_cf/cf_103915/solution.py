"""
QUESTION:
Write a function named `convert_string` that takes a string as input and returns the string with all letters converted to lowercase and all spaces replaced with underscores.
"""

def convert_string(s):
    return s.lower().replace(" ", "_")