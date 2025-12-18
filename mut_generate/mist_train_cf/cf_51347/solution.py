"""
QUESTION:
Convert a given mathematical expression to the postfix notation including nested parentheses and exponential calculations, giving priority to parentheses, then exponential calculations, followed by multiplication and division, and finally addition and subtraction. Implement the function `infix_to_postfix(expression)` that takes a string `expression` as input, where the string contains the mathematical expression in infix notation, and returns the corresponding postfix notation as a string. The function should handle nested parentheses and the following operators: `+`, `-`, `*`, `/`, and `^`.
"""

class Operator:
    def __init__(self, precedence, associativity):
        self.precedence = precedence
        self.associativity = associativity

operators = {
    '+': Operator(1, 'L'),
    '-': Operator(1, 'L'),
    '*': Operator(2, 'L'),
    '/': Operator(2, 'L'),
    '^': Operator(3, 'R'),
    '(': Operator(0, ''),
    ')': Operator(0, ''),
}

def entance(expression):
    output = ''
    stack = []  

    for char in expression:
        if char.isspace():
            continue
        if char not in operators:
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and ((operators[char].associativity == 'L' and operators[char].precedence <= operators[stack[-1]].precedence) or (operators[char].associativity == 'R' and operators[char].precedence < operators[stack[-1]].precedence)):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output