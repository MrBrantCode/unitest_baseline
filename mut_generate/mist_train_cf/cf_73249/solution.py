"""
QUESTION:
Write a function `parse_expr(expression)` that parses a given mathematical expression to create a stack data structure. The expression can include floating point numbers and negative values, and supports unary operators. The function should return the parsed expression in Reverse Polish Notation (RPN).
"""

import math
import operator as op

OPERATORS = {
    '+': (1, op.add),
    '-': (1, op.sub),
    '*': (2, op.mul),
    '/': (2, op.truediv),
    '^': (3, op.pow),
}

def parse_expr(expression):
    def parse_token(token):
        try:
            return float(token)
        except ValueError:
            return token

    def tokenize(expression):
        token = ''
        for char in expression:
            if char in OPERATORS or char in "()":
                if token:
                    yield parse_token(token)
                    token = ''
                yield parse_token(char)
            else:
                token += char
        if token:
            yield parse_token(token)

    def shunting_yard(parsed):
        stack = []
        for token in parsed:
            if type(token) is float:
                yield token
            elif token in OPERATORS:
                while (stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]):
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    yield stack.pop()
                stack.pop()
            elif token == "(":
                stack.append(token)
        while stack:
            yield stack.pop()

    return list(shunting_yard(tokenize(expression)))