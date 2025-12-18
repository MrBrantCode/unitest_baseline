"""
QUESTION:
Create a function named `get_argument_type` that takes one argument and returns a string describing the type of the argument. The function should identify the argument as 'string', 'integer', 'float', 'list', or 'dictionary' based on its type.
"""

def get_argument_type(arg):
    if isinstance(arg, str):
        return 'string'
    if isinstance(arg, int):
        return 'integer'
    if isinstance(arg, float):
        return 'float'
    if isinstance(arg, list):
        return 'list'
    if isinstance(arg, dict):
        return 'dictionary'