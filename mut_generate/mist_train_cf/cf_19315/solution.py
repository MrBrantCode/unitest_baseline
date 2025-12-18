"""
QUESTION:
ClassifyExpressionType function should take an arithmetic expression as input and return the type of the expression. The input expression is expected to be a string containing integers, arithmetic operators (+, -, *, /, %), and parentheses. The function should ignore any whitespace characters in the input expression.
"""

def classify_expression(expression):
    expression = expression.replace(" ", "")
    if "(" in expression:
        return "parenthesized"
    elif "/" in expression or "%" in expression:
        return "rational"
    elif "+" in expression or "-" in expression:
        return "polynomial"
    elif "*" in expression:
        return "polynomial"
    else:
        return "constant"