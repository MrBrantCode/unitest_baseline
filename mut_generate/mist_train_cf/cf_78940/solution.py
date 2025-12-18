"""
QUESTION:
Write a function `solution(infix_expressions)` that takes a list of mathematical expressions in infix notation as input, converts them into postfix notation, and returns a dictionary with the infix expressions as keys and the corresponding postfix expressions as values. The function should be able to handle multi-digit integers and the four standard arithmetic operations (+, -, *, /). Ignore the possibility of division by zero.
"""

class Converter:
    def __init__(self, capacity):
        self.top = -1
        self.stack = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        self.result = []
        self.capacity = capacity

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def isOperand(self, ch):
        return ch.isalnum()

    def notGreater(self, i):
        try:
            return True if self.precedence[i] <= self.precedence[self.peek()] else False
        except KeyError: 
            return False
          
    def infixToPostfix(self, expression):    
        for i in expression:
            if self.isOperand(i):
                self.result.append(i)
            elif i  == '(':
                self.stack.append(i)
            elif i == ')':
                while self.stack and self.stack[-1]  != '(':
                    self.result.append(self.stack.pop())
                self.stack.pop()
            else:
                while self.stack and self.stack[-1] != '(' and self.notGreater(i):
                    self.result.append(self.stack.pop())
                self.stack.append(i)
        while self.stack:
            self.result.append(self.stack.pop())
        return ' '.join(self.result)

def entance(infix_expressions):
    expression_map = {}
    for expression in infix_expressions:
        split_expression = expression.split()
        converter = Converter(len(split_expression))
        postfix_expression = converter.infixToPostfix(split_expression)
        expression_map[expression] = postfix_expression
    return expression_map