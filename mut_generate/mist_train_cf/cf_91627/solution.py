"""
QUESTION:
Write a function `detect_python_version` that takes a string representing a Python script as input and returns the Python version number as a string that the script is compatible with. The function should analyze the script's compatibility based on its contents without executing it, and it should handle scripts with syntax errors or unsupported features by returning "Python version not supported".
"""

import ast

class VersionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.version = None

    def visit_If(self, node):
        if isinstance(node.test, ast.Compare):
            left = node.test.left
            if isinstance(left, ast.Attribute) and isinstance(left.value, ast.Attribute):
                if left.value.value.id == 'sys' and left.value.attr == 'version_info':
                    if isinstance(node.test.comparators[0], ast.Tuple):
                        comparators = node.test.comparators[0].elts
                        if len(comparators) == 2:
                            major = comparators[0].n
                            minor = comparators[1].n
                            self.version = f"Python {major}.{minor} or higher required"

def detect_python_version(script):
    try:
        tree = ast.parse(script)
        visitor = VersionVisitor()
        visitor.visit(tree)
        return visitor.version
    except SyntaxError:
        return "Python version not supported"