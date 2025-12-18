"""
QUESTION:
Implement a function called `determine_type` that takes one argument `value` of any type and returns an integer indicating the type of the value. The function should return 4 if the input value is an integer, 1 if it is a string, and 0 otherwise.
"""

def determine_type(value: any) -> int:
    if isinstance(value, int):
        return 4
    elif isinstance(value, str):
        return 1
    else:
        return 0