"""
QUESTION:
Design a function `validate_expression` that takes a string `expr` representing a mathematical expression and returns `True` if the expression is correctly formatted with balanced parentheses, correct operator precedence, and contains only numbers, operators, parentheses, and valid mathematical functions (sin, cos, tan, log, sqrt), and `False` otherwise. The function should handle nested mathematical functions and follow these restrictions:
- Only consider seven basic arithmetic operations: addition, subtraction, multiplication, division, exponentiation, parentheses, and functions.
- Division and multiplication have equal priority.
- Whitespaces are not valid in the expressions.
- Negative numbers are considered but should be in the format "-2", not "- 2" or "2 -".
"""

import re

def validate_expression(expr):
    # define valid characters, operators, and functions
    VALID_CHARS = set("0123456789+-*/()^.")
    VALID_OPERATORS = set("-+*/^")
    VALID_FUNCTIONS = set(["sin", "cos", "tan", "log", "sqrt"])

    # define regex for number and function matching
    NUMBER_RE = r"(-?\d+(\.\d+)?)"
    FUNCTION_RE = r"(" + "|".join(VALID_FUNCTIONS) + ")"

    # validate characters in the expression
    if not set(expr).issubset(VALID_CHARS):
        return False

    # validate parentheses balancing using a stack
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False

    # validate numbers and functions using regex
    for part in re.split("[^a-z0-9.]+", expr):
        if part and not (re.fullmatch(NUMBER_RE, part) or re.fullmatch(FUNCTION_RE, part)):
            return False

    # validate operator precedence
    prior_operator = ""
    for i, char in enumerate(expr):
        if char in VALID_OPERATORS and i != 0 and expr[i-1] in VALID_OPERATORS:
            if not (char == "-" and prior_operator != "^"):
                return False
        if char == "^":
            prior_operator = char
        else:
            prior_operator = ""
    return True