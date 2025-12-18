"""
QUESTION:
Create a function `checkBalanced` that takes a string `expression` as input and returns a boolean value indicating whether the braces in the expression are balanced. The function should consider the following types of braces: `()`, `[]`, and `{}`.
"""

def checkBalanced(expression):
    """
    This function checks if the braces in a given expression are balanced.
    
    Args:
        expression (str): A string containing the expression to be checked.
    
    Returns:
        bool: True if the expression is balanced, False otherwise.
    """
    
    s = []
    for i in expression:
        if i == '(' or i == '[' or i == '{': 
            s.append(i)
        elif i == ')' or i == ']' or i == '}':
            if len(s) > 0 and (
                (i == ')' and s[len(s)-1] == '(') or 
                (i == ']' and s[len(s)-1] == '[') or 
                (i == '}' and s[len(s)-1] == '{')):
                s.pop()
            else:
                return False
    return len(s) == 0