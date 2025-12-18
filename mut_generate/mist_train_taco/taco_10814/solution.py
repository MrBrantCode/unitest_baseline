"""
QUESTION:
Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

should return false:
"""

def is_valid_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False