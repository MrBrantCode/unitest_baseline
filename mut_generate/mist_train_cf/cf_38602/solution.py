"""
QUESTION:
Evaluate the result of a simplified spreadsheet formula. Implement a function `evaluate_formula(formula: str) -> float` that takes a string formula as input, evaluates it from left to right with functions taking precedence over operations, and returns the result. The formula consists of addition, subtraction, multiplication, division operations, and `RefreshAll()` and `quit()` functions, separated by spaces. The `RefreshAll()` function should be executed but its result is not included in the final output, and the `quit()` function should be executed but its result is not included in the final output.
"""

def evaluate_formula(formula: str) -> float:
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    functions = {'RefreshAll()': lambda: None, 'quit()': lambda: None}

    tokens = formula.split()
    result = 0
    current_op = '+'
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in operations:
            current_op = token
        elif token in functions:
            functions[token]()
        else:
            operand = float(token)
            if current_op in operations:
                result = operations[current_op](result, operand)
        i += 1

    return result