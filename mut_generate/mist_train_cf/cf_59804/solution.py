"""
QUESTION:
Implement a function called `check_math_expression` that validates a given mathematical expression. The function should take a string `expr` representing the mathematical expression as an input and return `True` if the expression is valid and `False` otherwise. The function should allow the use of standard mathematical operations and functions, including `sqrt`, `log`, `sin`, `cos`, `tan`, `pi`, and `e` from the math library. If the expression contains any invalid operations, syntax errors, division by zero, or other mathematical errors, the function should return `False`.
"""

import math

def check_math_expression(expr):
    '''
    Function to check a mathematical expression.

    Parameters:
    expr (str): mathematical expression.

    Returns:
    result (bool): If mathematical expression is valid it returns True else False.
    '''
    try:
        # List of valid operations, functions and constants
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("_ ")
        }
    
        allowed_names.update({
            'sqrt': math.sqrt, 'log': math.log, 'sin': math.sin, 'cos': math.cos, 
            'tan': math.tan, 'pi': math.pi, 'e': math.e
        })
        
        # Create a safe dictionary and add the allowed operations, functions, and constants 
        safe_dict = {'__builtins__': None}
        safe_dict.update(allowed_names)
        
        # Check if the expression is valid
        eval(expr, {"__builtins__": None}, safe_dict)
        return True

    except (SyntaxError, NameError, ZeroDivisionError, TypeError):
        return False