"""
QUESTION:
Write a function named `check_strings` that takes a list of strings as input. The function should return True if any string in the list starts with "t" and has a length greater than 3. If no such string is found, the function should return False.
"""

def check_strings(lst):
    for string in lst:
        if string.startswith("t") and len(string) > 3:
            return True
    return False