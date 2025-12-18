"""
QUESTION:
Write a function `track_function_calls` that takes a string of Python code as input and returns a dictionary where the keys are function names and the values are the number of times each function is called in the given code. The function should exclude built-in Python functions and only track user-defined function calls.
"""

import ast
from collections import defaultdict

def track_function_calls(code):
    """
    This function takes a string of Python code as input and returns a dictionary 
    where the keys are function names and the values are the number of times each 
    function is called in the given code. The function excludes built-in Python 
    functions and only tracks user-defined function calls.

    Args:
        code (str): A string of Python code.

    Returns:
        dict: A dictionary with function names as keys and their call counts as values.
    """

    # Parse the code into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize a dictionary to store function call counts
    function_calls = defaultdict(int)

    # Iterate over all nodes in the abstract syntax tree
    for node in ast.walk(tree):
        # Check if the node is a function call
        if isinstance(node, ast.Call):
            # Check if the function is user-defined (not built-in)
            if isinstance(node.func, ast.Name) and not node.func.id.startswith('__'):
                # Increment the function call count
                function_calls[node.func.id] += 1

    return dict(function_calls)