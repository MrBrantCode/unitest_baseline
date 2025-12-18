"""
QUESTION:
Create a function named `check_expression` that validates whether a given mathematical expression in string format is correctly formatted and follows mathematical rules such as order of operations, integer division, and modulo operations. The function should handle any type of valid mathematical expression, including the use of functions and variables. The function should return `True` if the expression is valid and `False` otherwise, along with an error message if the expression is invalid.
"""

import ast

class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_BinOp(self, node):
        if not (isinstance(node.op, ast.Add) or
                isinstance(node.op, ast.Sub) or
                isinstance(node.op, ast.Mult) or
                isinstance(node.op, ast.Div) or
                isinstance(node.op, ast.FloorDiv) or
                isinstance(node.op, ast.Mod)):
            self.errors.append(f"Unsupported operator at lineno {node.lineno}")
        self.generic_visit(node)

def check_expression(expr_str):
    try:
        tree = ast.parse(expr_str)
    except SyntaxError as e:
        return False, str(e)
    visitor = Visitor()
    visitor.visit(tree)
    if visitor.errors:
        return False, visitor.errors
    else:
        return True, "This expression is valid"