"""
QUESTION:
Write a function to match strings that start with "abc" and end with "xyz". The function should return a regex pattern that matches the given condition.
"""

def entrance(s):
    import re
    return bool(re.match(r"^abc.*xyz$", s))