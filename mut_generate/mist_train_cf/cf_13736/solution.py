"""
QUESTION:
Create a regular expression pattern that matches any string that starts with a lowercase letter and contains at least one digit.
"""

def entrance(s):
    pattern = r"^[a-z].*\d"
    if s:
        return bool(re.match(pattern, s))
    else:
        return False