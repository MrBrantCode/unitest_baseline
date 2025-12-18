"""
QUESTION:
Implement a Python function `process_arguments` that takes a list of arguments as input. The function must assert the list has a size equal to 1, extract a single value from the list, and return a tuple containing the extracted value.
"""

def process_arguments(args):
    assert len(args) == 1
    value, = args
    return (value,)