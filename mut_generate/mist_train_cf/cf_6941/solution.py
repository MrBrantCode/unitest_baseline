"""
QUESTION:
Create a function named `evaluate_expression` that evaluates a mathematical expression given as a string. The string can contain addition (+), subtraction (-), multiplication (*), division (/), exponentiation (^), and modulus (%) operators. It can also contain floating-point numbers and variables represented by a single letter. The expression can have multiple levels of parentheses and nested expressions. The function should return the result of the evaluated expression as a float.
"""

def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    
    operands = []
    operators = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 3}
    
    temp = ""
    for char in expression:
        if char.isdigit() or char == ".":
            temp += char
        else:
            if temp != "":
                operands.append(float(temp))
                temp = ""
            if char in precedence:
                while len(operators) > 0 and operators[-1] != "(" and precedence[char] <= precedence[operators[-1]]:
                    operands.append(operators.pop())
                operators.append(char)
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while len(operators) > 0 and operators[-1] != "(":
                    operands.append(operators.pop())
                if len(operators) > 0 and operators[-1] == "(":
                    operators.pop()
    
    if temp != "":
        operands.append(float(temp))
    
    while len(operators) > 0:
        operands.append(operators.pop())
    
    stack = []
    for element in operands:
        if isinstance(element, float) or element.isalpha():
            stack.append(element)
        else:
            if element == "^":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 ** operand2
                stack.append(result)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if element == "+":
                    result = operand1 + operand2
                elif element == "-":
                    result = operand1 - operand2
                elif element == "*":
                    result = operand1 * operand2
                elif element == "/":
                    result = operand1 / operand2
                elif element == "%":
                    result = operand1 % operand2
                stack.append(result)
    
    return stack[0]