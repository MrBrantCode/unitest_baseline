"""
QUESTION:
Create a recursive function `modify_string(s)` that takes a string `s` and returns a new string containing only the characters at odd index locations (1, 3, 5, etc.) while discarding the characters at even index locations (0, 2, 4, etc.). The function should handle strings of any length, including empty strings.
"""

def modify_string(s: str) -> str:
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return ""
    else:
        return s[1] + modify_string(s[2:])