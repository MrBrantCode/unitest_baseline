"""
QUESTION:
Create a function named `find_mixed_case_strings` that takes a list of strings as input and returns a new list containing only the strings that have both uppercase and lowercase letters.
"""

def find_mixed_case_strings(strings):
    return [string for string in strings if any(c.islower() for c in string) and any(c.isupper() for c in string)]