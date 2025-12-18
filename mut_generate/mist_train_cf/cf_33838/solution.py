"""
QUESTION:
Implement a function `check_lambda_expression` that takes an annotated lambda expression as input and verifies if the evaluation tree matches the expected structure. The annotation is a special comment that starts with `# CHECK-TREE:` followed by a JSON-like representation of the expected evaluation tree. The input expression is a string of length between 1 and 1000 characters. The function should return a boolean value indicating whether the evaluation tree of the lambda expression matches the expected structure.
"""

import re
import ast

def check_lambda_expression(expression: str) -> bool:
    # Extract the annotated evaluation tree from the expression
    match = re.search(r'# CHECK-TREE: (.+)', expression)
    if match:
        expected_tree = match.group(1)
    else:
        return False  # Annotation not found

    # Extract the lambda expressions and variable assignments
    assignments = {}
    for line in expression.split('\n'):
        if '=' in line:
            var, expr = line.split('=')
            assignments[var.strip()] = expr.strip()

    # Evaluate the lambda expressions and build the actual evaluation tree
    actual_tree = {}
    for var, expr in assignments.items():
        if var != 'expression':
            try:
                value = ast.literal_eval(expr)
                actual_tree[var] = value
            except (SyntaxError, ValueError):
                return False  # Invalid expression format

    # Compare the expected and actual evaluation trees
    try:
        return actual_tree == ast.literal_eval(expected_tree)
    except (SyntaxError, ValueError):
        return False  # Invalid expected tree format