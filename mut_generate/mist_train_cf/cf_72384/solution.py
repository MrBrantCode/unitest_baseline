"""
QUESTION:
f is_happy(s):
    """A string is happy if its length is between 3 and 100 characters, 
    every 3 consecutive letters are distinct, and every distinct letter appears at least twice.
    Implement this function to return True if the string is happy and False otherwise."""
"""

def is_happy(s):
    if not (3 <= len(s) <= 100):
        return False
    distinct_letters = set(s)
    for letter in distinct_letters:
        if s.count(letter) < 2:
            return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True