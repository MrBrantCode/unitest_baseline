"""
QUESTION:
Convert a postfix expression to an infix expression without using any built-in functions or libraries, implementing your own stack data structure. Write a function `postfix_to_infix(postfix_expression)` that takes a string `postfix_expression` as input and returns the equivalent infix expression as a string.
"""

def postfix_to_infix(postfix_expression):
    class Stack:
        def __init__(self):
            self.items = []
        
        def is_empty(self):
            return self.items == []
        
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            else:
                return None
    
    # Initialize an empty stack
    stack = Stack()
    
    # Start scanning the postfix expression from left to right
    for char in postfix_expression:
        # If the character is an operand, push it onto the stack
        if char.isdigit():
            stack.push(char)
        # If the character is an operator, pop the top two operands from the stack
        elif char in "+-*/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Construct an infix expression by combining the popped operands, operator, and appropriate parentheses
            infix_expression = f"({operand1} {char} {operand2})"
            # Push the newly constructed infix expression back onto the stack
            stack.push(infix_expression)
    
    # After scanning the entire postfix expression, the final infix expression will be present on the top of the stack
    return stack.pop()