"""
QUESTION:
Given a Python file, create a function `parsePythonCode` to read and parse the file in JavaScript, allowing access to different node types and their values, similar to what RedBaron provides in Python. The function should not rely on line-by-line reading, as it is insufficient for the required functionality. Consider using a JavaScript library that can parse or manipulate Python code, or an alternative solution that leverages Python's built-in `ast` module or other tools such as Filbert or Skulpt.
"""

import ast

def parsePythonCode(code):
    """
    Parse Python code into an Abstract Syntax Tree.
    
    Args:
        code (str): The Python code to parse.
    
    Returns:
        ast.Module: The parsed Abstract Syntax Tree.
    """
    return ast.parse(code)