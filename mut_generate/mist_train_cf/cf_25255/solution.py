"""
QUESTION:
Evaluate the value of an expression written in reverse Polish notation. 

Function Name: Not specified
Input: A list of strings representing the expression in reverse Polish notation.
Restrictions: The input expression is valid, and the numbers are non-negative integers.
 
For example, given the expression ["5", "1", "2", "+", "4", "*", "+", "3", "-"], calculate the final result.
"""

def evalRPN(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            else:
                result = int(operand1 / operand2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()