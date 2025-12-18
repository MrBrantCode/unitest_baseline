"""
QUESTION:
Create a function named `analyze_code(code)` that analyzes the syntactical structure of the input Python `code` string and categorizes its type. The function should be able to identify if the code is a function declaration, conditional statement, or loop statement, among other programming constructs. It should also dissect the code and extract key components such as the function name, arguments, and return statement. The function should not execute the input code.
"""

import ast

def analyze_code(code):
    parsed = ast.parse(code)
    if isinstance(parsed, ast.Module):
        for node in ast.iter_child_nodes(parsed):
            if isinstance(node, ast.FunctionDef):
                arguments = [arg.arg for arg in node.args.args]
                return_statement = ''
                for sub_node in ast.iter_child_nodes(node):
                    if isinstance(sub_node, ast.Return):
                        return_statement = ast.unparse(sub_node.value)
                return {
                    'construct': 'Function Declaration',
                    'function_name': node.name,
                    'arguments': arguments,
                    'return_statement': return_statement,
                }
    return 'Invalid or Unsupported Code Snippet'