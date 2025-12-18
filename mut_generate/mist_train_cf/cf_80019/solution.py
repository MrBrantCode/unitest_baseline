"""
QUESTION:
Write a function named infix_to_rpn that takes an expression as input and returns its equivalent Reverse Polish Notation (RPN) expression. The expression may contain operands (letters) and operators (+, -, *, /, ^). The function should follow the order of operations and use the standard operator precedence rules.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, char):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

def precedence(operator):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    return prec[operator]

def is_operator(char):
    operators = set(["+", "-", "*", "/", "^"])
    return char in operators

def infix_to_rpn(expression):
    stack = Stack()

    rpn = ""
    for char in expression:
        if is_operator(char):
            while (not stack.is_empty() and is_operator(stack.stack[-1]) and 
                   precedence(char) <= precedence(stack.stack[-1])):
                rpn += stack.pop()
            stack.push(char)
        else:  
            rpn += char
            
    while not stack.is_empty():
        rpn += stack.pop() 
  
    return rpn