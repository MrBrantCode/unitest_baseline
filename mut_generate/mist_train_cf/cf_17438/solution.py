"""
QUESTION:
Write a function called `get_data_type` that takes an input string containing any valid Python object and returns one of the following strings: "integer", "float", "boolean", "string", "list", "tuple", "set", "dictionary", "function", "module". The function should handle both single-line and multi-line strings, circular references within nested objects, and invalid Python expressions, and should have a time complexity of O(n), where n is the length of the input string.
"""

import ast

def get_data_type(input_string):
    try:
        node = ast.parse(input_string)
        data_type = type(ast.literal_eval(input_string)).__name__
        return data_type
    except (SyntaxError, ValueError):
        try:
            data_type = type(eval(input_string)).__name__
            if data_type in ['function', 'module']:
                return data_type
        except Exception:
            return 'string'