"""
QUESTION:
Create a function `bracket_parser(expr)` that takes a string `expr` representing a mathematical expression with varied brackets like '()', '[]', and '{}' as input. The function should validate if the arrangement of brackets in the expression is balanced and evaluate the valid expression. If the expression is valid, return the evaluated result; otherwise, return 'Expression Invalid'.
"""

def bracket_parser(expr):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    for char in expr:
        if char in brackets.values():  # If character is an opening bracket
            stack.append(char)
        elif char in brackets.keys():  # If character is a closing bracket
            if stack and brackets[char] == stack[-1]:  
                stack.pop()  
            else:  
                return 'Expression Invalid'  
    
    if stack:  # If some brackets are not closed
        return 'Expression Invalid'
    
    try:   
        result = eval(expr)  # Evaluate the expression
        return result
    except:
        return 'Expression Invalid'