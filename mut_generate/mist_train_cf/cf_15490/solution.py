"""
QUESTION:
Write a function `find_string` that takes two parameters: a list of strings `strings` and a set of special characters `special_chars`. The function should iterate over `strings` and return the first string that contains both uppercase and lowercase letters, as well as at least one character from `special_chars`. If no such string is found, return `None`.
"""

def find_string(strings, special_chars):
    for string in strings:
        contains_upper = any(c.isupper() for c in string)
        contains_lower = any(c.islower() for c in string)
        contains_special = any(c in special_chars for c in string)

        if contains_upper and contains_lower and contains_special:
            return string
    return None