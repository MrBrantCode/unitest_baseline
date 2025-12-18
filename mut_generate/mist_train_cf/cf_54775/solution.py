"""
QUESTION:
Design a function `evaluate_expression(exp)` that takes a string `exp` representing a mathematical expression and returns the result of the expression. The function must verify that the expression is correctly formatted with balanced parentheses and handles negative numbers, floating-point numbers, addition, subtraction, multiplication, division, and power operations. The function should also detect and handle division by zero errors and raise errors for incorrect expression format, invalid literals, and unsupported operand types.
"""

def evaluate_expression(exp):
    try:
        # Verifying the balance of parentheses
        if exp.count('(') != exp.count(')'):
            return "error: unbalanced parentheses"
        
        # Handling the possibility of division by zero
        if "/0" in exp:
            return "error: division by zero"
        
        # Evaluating the expression
        return eval(exp)
    except SyntaxError:
        return "error: incorrect expression format"
    except NameError:
        return "error: invalid literal"
    except TypeError:
        return "error: unsupported operand type"
    except ZeroDivisionError:
        return "error: division by zero"