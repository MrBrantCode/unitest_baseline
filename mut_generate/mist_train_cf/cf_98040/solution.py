"""
QUESTION:
Write a function `solve_equations(equations)` that takes a list of equations with missing operators as input. The function should return `True` if all equations are true when the missing operator is replaced with one of the four basic arithmetic operators (+, -, *, /) and `False` otherwise. The input equations will be in the format "number _ number = result".
"""

def solve_equations(equations):
    for equation in equations:
        parts = equation.split()
        num1 = int(parts[0])
        num2 = int(parts[2])
        result = int(parts[4])
        if num1 + num2 == result or num1 - num2 == result or num1 * num2 == result or num1 / num2 == result:
            continue
        else:
            return False
    return True