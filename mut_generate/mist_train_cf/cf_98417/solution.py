"""
QUESTION:
Write a function that takes a string as input and returns all the matches of the pattern "(?<=\=)\d+" using re.findall.
"""

def entrance(s):
    import re
    pattern = r"(?<=\=)\d+"
    return re.findall(pattern, s)