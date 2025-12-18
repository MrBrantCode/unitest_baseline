"""
QUESTION:
Implement a function `parse_function_declaration(code)` that takes a string `code` representing a function declaration as input and returns a dictionary containing the parsed function name and parameters. The dictionary should have two keys: "function_name" and "parameters", where "function_name" is the name of the function and "parameters" is a list of parameter names. The function should support function declarations with optional parameters.
"""

import re

def parse_function_declaration(code):
    pattern = r'function\s+(\w+)\s*\(([^)]*)\)'
    match = re.match(pattern, code)
    if match:
        function_name = match.group(1)
        parameters = [param.strip() for param in match.group(2).split(',') if param.strip()]
        return {"function_name": function_name, "parameters": parameters}
    else:
        return None