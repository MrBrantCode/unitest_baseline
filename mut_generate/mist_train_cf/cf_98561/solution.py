"""
QUESTION:
Create a function `detect_operators` that takes a dictionary of mathematical equations as input where each equation is a string in the format "x operator y = z". The function should return a dictionary where the keys are the equation names and the values are the operators used in each equation. The input dictionary can contain any number of equations and any valid mathematical operators (+, -, \*, /, %, ^, //).
"""

def detect_operators(equations):
    operators = {}
    for key, value in equations.items():
        equation = value.split()
        operators[key] = equation[1]
    return operators