"""
QUESTION:
Create a function `looks_falsy` that determines whether a given input "looks falsy" based on Python's truth value testing rules. The function should handle the following cases: 
- Strings: consider falsy if, when converted to lowercase and stripped of leading/trailing whitespace, the string matches 'false'.
- Integers: consider falsy if the integer equals 0.
- Lists: consider falsy if the list is empty or contains only other falsy values.
For all other types, consider the value truthy.
"""

def looks_falsy(value):
    if isinstance(value, str):
        return value.strip().lower() == 'false'
    elif isinstance(value, int):
        return value == 0
    elif isinstance(value, list):
        return len(value) == 0 or all(looks_falsy(item) for item in value)
    else:
        return False  