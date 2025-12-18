"""
QUESTION:
Write a function `track_function_calls` that takes a string of Python code as input and returns a dictionary where the keys are the names of the functions called in the code and the values are the number of times each function is called. The function should be able to handle nested function calls and function calls with varying numbers of arguments, and it should exclude built-in functions. The code may contain function definitions, but these should not be counted as function calls.
"""

import ast

def track_function_calls(code):
    """
    Track function calls in a given Python code string.

    Args:
    code (str): A string of Python code.

    Returns:
    dict: A dictionary where the keys are the names of the functions called in the code
          and the values are the number of times each function is called.
    """
    tree = ast.parse(code)
    calls = {}

    def extract_calls(node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if not hasattr(__builtins__, func_name):
                    calls[func_name] = calls.get(func_name, 0) + 1
        for child in ast.iter_child_nodes(node):
            extract_calls(child)

    extract_calls(tree)
    return calls