"""
QUESTION:
Create a function `solve_equations` that takes an array of mathematical equations as strings, evaluates each equation, and returns the results. Each equation may contain parentheses and the operations +, -, *, /, and ^ (exponentiation), where ^ should be treated as Python's ** operator. Note that the input equations are trusted and do not pose a risk of arbitrary code execution.
"""

def solve_equations(equations):
    results = []
    for equation in equations:
        equation = equation.replace('^', '**')
        results.append(eval(equation))

    return results