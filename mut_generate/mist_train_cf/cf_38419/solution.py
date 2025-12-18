"""
QUESTION:
Implement a function `resolve_camel_case(name)` that takes a string `name` as input and returns the string with camel case resolved by inserting spaces before capital letters, except for the first letter of the string.
"""

def resolve_camel_case(name):
    resolved_name = ""
    for i, char in enumerate(name):
        if i > 0 and char.isupper():
            resolved_name += " " + char
        else:
            resolved_name += char
    return resolved_name