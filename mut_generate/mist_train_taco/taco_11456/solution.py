"""
QUESTION:
Notes

Template in C

Constraints

2 ≤ the number of operands in the expression ≤ 100
1 ≤ the number of operators in the expression ≤ 99
-1 × 109 ≤ values in the stack ≤ 109

Input

An expression is given in a line. Two consequtive symbols (operand or operator) are separated by a space character.

You can assume that +, - and * are given as the operator and an operand is a positive integer less than 106

Output

Print the computational result in a line.

Examples

Input

1 2 +


Output

3


Input

1 2 + 3 4 - *


Output

-3
"""

def evaluate_rpn(expression: str) -> int:
    """
    Evaluates a given Reverse Polish Notation (RPN) expression and returns the result.

    Parameters:
    expression (str): A string representing the RPN expression. Operands and operators are separated by spaces.

    Returns:
    int: The result of evaluating the RPN expression.
    """
    ope = {'+': lambda a, b: b + a, '-': lambda a, b: b - a, '*': lambda a, b: b * a}
    stack = list()
    
    for c in expression.split():
        if c in ope:
            stack.append(ope[c](stack.pop(), stack.pop()))
        else:
            stack.append(int(c))
    
    return stack[-1]