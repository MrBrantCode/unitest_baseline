"""
QUESTION:
Write a function `evaluateExpressions` that takes a list of strings representing mathematical expressions and returns a list of integers representing the evaluated results. Each expression is well-formed, contains no syntax errors, and may include numbers, arithmetic operators (+, -, *, /), and parentheses. The function should return the results of evaluating each expression.
"""

from typing import List

def evaluateExpressions(expressions: List[str]) -> List[int]:
    return [eval(expression.replace(" ", "").replace("x", "*")) for expression in expressions]