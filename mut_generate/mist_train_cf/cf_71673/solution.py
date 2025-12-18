"""
QUESTION:
Write a function `postfix_calc(postfix)` that takes a string `postfix` representing an expression in postfix notation and returns the computed result of the expression. The string contains integers and operators (+, -, *, /, ^), where ^ denotes exponentiation and is right associative. The input string is space-separated.
"""

def postfix_calc(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    postfix = postfix.split()

    for char in postfix:
        if char not in operators:
            stack.append(int(char))
        else:
            if char=='^':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1**num2
            if char=='*':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1*num2
            elif char=='/':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1/num2
            elif char=='+':
                result = stack.pop() + stack.pop()
            elif char=='-':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1 - num2
            stack.append(result)

    return stack[0]