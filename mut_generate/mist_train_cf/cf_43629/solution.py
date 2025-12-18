"""
QUESTION:
Create a function `prefixToPostfix(prefix)` that takes a string `prefix` representing a prefix expression and returns the equivalent postfix expression as a string. The function should use a stack data structure to process the prefix expression.
"""

def prefixToPostfix(prefix):
    stack = []
    
    # Reading prefix string in reverse order
    for i in range(len(prefix)-1, -1, -1):
    
        # Check if symbol is operator
        if prefix[i] in ['+', '-', '*', '/']:
 
            # Take two operands from stack
            operand1 = stack[-1]
            stack.pop()
            operand2 = stack[-1]
            stack.pop()
           
            # append operand1, operand2 and operator
            stack.append(operand1 + operand2 + prefix[i])
        
        # if symbol is an operand
        else:
            stack.append(prefix[i])
     
 
    return stack.pop()