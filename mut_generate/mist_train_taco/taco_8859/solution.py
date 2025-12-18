"""
QUESTION:
Create an OR function, without use of the 'or' keyword, that takes an list of boolean values and runs OR against all of them.

Assume there will be between 1 and 6 variables, and return None for an empty list.
"""

def or_list(lst: list[bool]) -> bool | None:
    return any(lst) if lst else None