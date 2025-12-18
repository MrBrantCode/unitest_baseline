"""
QUESTION:
Create two functions, `prefixToInfix(prefix)` and `prefixToPostfix(prefix)`, that convert a given prefix expression into infix and postfix expressions, respectively. The prefix expression can include the operators '+', '-', '*', '/', and '^'. The functions should handle the conversion correctly, taking into account the order of operations and operator precedence.
"""

def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()

def prefixToPostfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = stack.pop() + stack.pop() + prefix[i]
            stack.append(str)
            i -= 1
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^":
        return True
    else:
        return False