"""
QUESTION:
Write a function called `check_module_imports` that takes a string of Python code as input and returns `True` if the code imports the "torch" module and its submodule "interpolatability", and `False` otherwise. The function should specifically check for the presence of "torch" and "interpolatability" within import statements in the given code snippet, regardless of any aliasing or other imports present.
"""

import ast

def check_module_imports(code: str) -> bool:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split('.')[0] == 'torch':
                    return True
        elif isinstance(node, ast.ImportFrom):
            if node.module == 'torch':
                for alias in node.names:
                    if alias.name == 'interpolatability':
                        return True
    return False