"""
QUESTION:
Create a function called `validate_methods` that takes a dictionary of methods and a regular expression pattern as input. The function should validate the method names against the given pattern, excluding "constructor" and "destructor" from validation. If a SyntaxError occurs during validation, the function should catch the exception and indicate its occurrence. The function should return a boolean value indicating whether all method names are valid according to the given pattern. The function should not re-raise the SyntaxError.
"""

import re

def validate_methods(methods: dict, pattern: str) -> bool:
    try:
        class_method_re = re.compile(pattern)
    except SyntaxError:
        return False

    for method_name, _ in methods.items():
        if method_name in ["constructor", "destructor"]:
            continue
        if not class_method_re.match(method_name):
            return False

    return True