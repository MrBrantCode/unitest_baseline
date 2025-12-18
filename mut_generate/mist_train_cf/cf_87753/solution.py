"""
QUESTION:
Write a function named `detect_python_version` that takes a string representing a Python script as input and returns the minimum required Python version as a string. The function should analyze the script's compatibility based on its contents without executing it. The script may contain syntax errors or unsupported features in certain Python versions.
"""

import ast

def detect_python_version(script):
    try:
        tree = ast.parse(script)
    except SyntaxError:
        return "Syntax error: Invalid Python script"

    import_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.Import)]
    version_required = None

    for import_node in import_nodes:
        for alias in import_node.names:
            if alias.name == 'sys':
                version_required = extract_version_from_ast_node(import_node)
                break

    if version_required is None:
        return "Python version not supported"
    elif version_required >= (3, 9):
        return "Python 3.9 or higher required"
    elif version_required >= (3, 8):
        return "Python 3.8 or higher required"
    elif version_required >= (3, 7):
        return "Python 3.7 or higher required"
    else:
        return "Python version not supported"

def extract_version_from_ast_node(node):
    for item in node.names:
        if item.name == 'version_info':
            if isinstance(item.asname, ast.Name):
                return (int(item.asname.id),)
            elif isinstance(item.asname, ast.Tuple):
                return tuple(int(num.n) for num in item.asname.elts)
    return None