"""
QUESTION:
Example

Input

1+2*3+4
11


Output

M
"""

def evaluate_expression(expression: str, expected_result: int) -> str:
    # Evaluate the expression using eval (for comparison)
    evaluated_result = eval(expression)
    
    # Compute the result by iterating through the expression
    computed_result = int(expression[0])
    for i in range(1, len(expression), 2):
        operator = expression[i]
        operand = int(expression[i + 1])
        if operator == '*':
            computed_result *= operand
        else:
            computed_result += operand
    
    # Determine the result based on the comparison
    if evaluated_result == expected_result and computed_result == expected_result:
        return 'M'
    elif computed_result == expected_result:
        return 'L'
    elif evaluated_result == expected_result:
        return 'U'
    else:
        return 'I'