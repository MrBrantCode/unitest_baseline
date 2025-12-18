"""
QUESTION:
Create a function `extract_imported_modules(code: str) -> dict` that takes a string `code` containing Python code snippets as input. The function should return a dictionary where the keys are the imported module names and the values are lists of the functions or classes imported from each module. The function should handle both `import` and `from ... import ...` statements.
"""

import ast

def extract_imported_modules(code: str) -> dict:
    imported_modules = {}

    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules[alias.name] = []
        elif isinstance(node, ast.ImportFrom):
            module_name = node.module
            imported_items = [alias.name for alias in node.names]
            if module_name in imported_modules:
                imported_modules[module_name].extend(imported_items)
            else:
                imported_modules[module_name] = imported_items

    return imported_modules