"""
QUESTION:
Implement a function `process` that takes a string representing a logical formula as input, where variables are single uppercase letters, and logical operators are "&&" for AND, "||" for OR, "!" for NOT, and "<=>" for equivalence. Return "Formula is satisfiable" if there exists a truth value assignment that makes the entire formula true, and "Formula is not satisfiable" otherwise.
"""

from itertools import product

def process(formula):
    def evaluate(expression, assignment):
        if len(expression) == 1:
            return assignment.get(expression, False)
        if expression[0] == '!':
            return not evaluate(expression[1:], assignment)
        if expression[1:3] == '&&':
            return evaluate(expression[0], assignment) and evaluate(expression[3:], assignment)
        if expression[1:3] == '||':
            return evaluate(expression[0], assignment) or evaluate(expression[3:], assignment)
        if expression[1:4] == '<=>':
            return evaluate(expression[0], assignment) == evaluate(expression[4:], assignment)

    variables = set(filter(str.isalpha, formula))
    for assignment in product([True, False], repeat=len(variables)):
        assignment_map = dict(zip(variables, assignment))
        if evaluate(formula, assignment_map):
            return "Formula is satisfiable"
    return "Formula is not satisfiable"