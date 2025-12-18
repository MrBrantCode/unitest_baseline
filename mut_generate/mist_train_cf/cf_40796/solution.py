"""
QUESTION:
Write a function `evaluateExpression` that evaluates a given mathematical expression represented as a string without spaces. The expression can contain the four basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/). The function should return the result of the evaluation as an integer.

The input expression will be a string of digits and operators, and the function should follow the order of operations (PEMDAS/BODMAS). The division operation should result in an integer, effectively rounding down the result. The function should be able to handle expressions of any length.
"""

def evaluateExpression(expression: str) -> int:
    stack = []
    num = 0
    sign = '+'
    for i in range(len(expression)):
        if expression[i].isdigit():
            num = num * 10 + int(expression[i])
        if (not expression[i].isdigit() and expression[i] != ' ') or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = expression[i]
            num = 0
    return sum(stack)