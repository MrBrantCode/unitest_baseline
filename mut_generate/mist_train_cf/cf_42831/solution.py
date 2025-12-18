"""
QUESTION:
Create a function `validate_ast` that takes in an abstract syntax tree (AST) node as input and returns `True` if the structure matches the specified pattern, and `False` otherwise. The pattern requires the node to be of type `ast.If`, have a `test` attribute of type `ast.Compare`, and have a `body` attribute containing exactly one element of type `ast.Expr`.
"""

import ast

def validate_ast(node):
    if not isinstance(node, ast.If):
        return False
    if not isinstance(node.test, ast.Compare):
        return False
    if len(node.body) != 1 or not isinstance(node.body[0], ast.Expr):
        return False
    return True