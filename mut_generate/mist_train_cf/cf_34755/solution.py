"""
QUESTION:
Implement a function `extract_info` that takes a single string parameter `function_str` representing a Python function definition. The function definition is expected to be in the format of `def function_name(self, other_parameters): ...`, where the function body contains a docstring enclosed in triple quotes. The function should extract the Python class name and the first character of the docstring, and return them as a tuple in the format `(class_name, first_char)`. If the class name is not present or the docstring is empty, the function should return `None` for the respective value.
"""

import re

def extract_info(function_str):
    class_name_match = re.search(r'def\s+([^\s(]+)\(', function_str)
    class_name = class_name_match.group(1) if class_name_match else None

    docstring_match = re.search(r'"""(.).*"""', function_str, re.DOTALL)
    first_char = docstring_match.group(1)[0] if docstring_match and docstring_match.group(1) else None

    return (class_name, first_char)