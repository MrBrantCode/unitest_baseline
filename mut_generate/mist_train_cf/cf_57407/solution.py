"""
QUESTION:
Implement the function `evalRPN(tokens)` that evaluates the value of an arithmetic expression in Reverse Polish Notation. The function takes a list of strings `tokens` as input, where each string represents either an operator or an operand. Valid operators are `+`, `-`, `*`, `/`, `^` (exponentiation), and `%` (modulus). The function should return the result of the given RPN expression. The input list `tokens` is guaranteed to be valid and will not contain division by zero operations.
"""

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/", "^", "%"]:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(int(num1 / float(num2)))
            elif token == "^":
                stack.append(num1 ** num2)
            elif token == "%":
                stack.append(num1 % num2)
        else:
            stack.append(int(token))
    return stack[0]