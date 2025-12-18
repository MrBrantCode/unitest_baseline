"""
QUESTION:
Implement a recursive function named `evaluate` that takes a mathematical expression as input, computes the result, and rounds it to the nearest whole number. The function should not use any loops or built-in arithmetic operators, except for the four basic mathematical operations: addition (+), subtraction (-), multiplication (*), and division (/). The time and space complexities of the function should be O(log n), where n is the value of the input expression.
"""

def evaluate(expression):
    if expression.isdigit():
        return int(expression)
    elif expression.startswith('(') and expression.endswith(')'):
        return evaluate(expression[1:-1])
    elif '*' in expression or '/' in expression:
        operator_index = 1
        while expression[operator_index] not in '*/':
            operator_index += 1
        
        operator = expression[operator_index]
        operand1 = evaluate(expression[:operator_index])
        operand2 = evaluate(expression[operator_index + 1:])
        
        if operator == '*':
            result = operand1 * operand2
        else:
            result = operand1 / operand2
        
        return round(result)
    elif '+' in expression or '-' in expression:
        operator_index = 1
        while expression[operator_index] not in '+-':
            operator_index += 1
        
        operator = expression[operator_index]
        operand1 = evaluate(expression[:operator_index])
        operand2 = evaluate(expression[operator_index + 1:])
        
        if operator == '+':
            result = operand1 + operand2
        else:
            result = operand1 - operand2
        
        return round(result)