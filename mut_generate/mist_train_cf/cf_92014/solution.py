"""
QUESTION:
Create a function `scientific_calculator(equation, decimal_places)` that takes a string `equation` containing a mathematical equation with operators (+, -, *, /) and functions (sin, cos, sqrt) and a positive integer `decimal_places` as input. The function should return the result of the equation, rounded to the specified `decimal_places`. The equation can contain both positive and negative numbers, decimal values, and parentheses. The function should prioritize the order of operations correctly.
"""

import math

def scientific_calculator(equation, decimal_places):
    equation = equation.replace(' ', '') # Remove spaces from the equation
    equation = equation.replace('sin', 'math.sin') # Replace sin with math.sin
    equation = equation.replace('cos', 'math.cos') # Replace cos with math.cos
    equation = equation.replace('sqrt', 'math.sqrt') # Replace sqrt with math.sqrt
    equation = equation.replace('^', '**') # Replace ^ with ** for exponentiation

    try:
        result = round(eval(equation), decimal_places) # Evaluate the equation and round the result
        return result
    except:
        return "Invalid equation"