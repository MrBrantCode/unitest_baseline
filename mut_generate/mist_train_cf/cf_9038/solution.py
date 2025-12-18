"""
QUESTION:
Implement a recursive function `recursive_calculation(expression)` that calculates a mathematical expression given as a list of numbers and operators, where the operators are '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division. The function should handle expressions with multiple operators and follow the order of operations (PEMDAS/BODMAS). The result should be rounded to the nearest whole number. The input expression is a list where each element is a number or an operator.
"""

def recursive_calculation(expression):
    if len(expression) == 1:
        return expression[0]
    
    if expression[1] == '+':
        return recursive_calculation([expression[0] + expression[2]] + expression[3:])
    elif expression[1] == '-':
        return recursive_calculation([expression[0] - expression[2]] + expression[3:])
    elif expression[1] == '*':
        return recursive_calculation([expression[0] * expression[2]] + expression[3:])
    elif expression[1] == '/':
        return recursive_calculation([expression[0] / expression[2]] + expression[3:])
    else:
        return recursive_calculation(expression[1:])