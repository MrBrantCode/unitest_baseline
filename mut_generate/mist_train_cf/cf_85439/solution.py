"""
QUESTION:
Implement two functions, `convertToPostfix` and `calculatePostfix`, to convert infix mathematical statements to postfix notation and calculate the result of the postfix notation, respectively.

The `convertToPostfix` function should take an infix mathematical statement as input, where the statement includes addition "+", subtraction "-", multiplication "*", division "/", parentheses "(", ")", and positive integers. The function should return the equivalent postfix notation as a string.

The `calculatePostfix` function should take a string in postfix notation as input and return the result of the mathematical expression.

Assume that all divisions are exact and the input is a valid mathematical expression. The implementation should consider the precedence and associativity of operators. Note that the input may contain single-digit integers only.
"""

def convertToPostfix(infix):
    PRECEDENCE = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    output = []
    operator_stack = []

    for char in infix:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and operator_stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(char)

    while operator_stack:
        output.append(operator_stack.pop())

    return ' '.join(output)

def calculatePostfix(postfix):
    stack = []

    for char in postfix.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            right = stack.pop()
            left = stack.pop()
            if char == '+':
                result = left + right
            elif char == '-':
                result = left - right
            elif char == '*':
                result = left * right
            elif char == '/':
                result = left / right
            stack.append(result)
    return stack[0]