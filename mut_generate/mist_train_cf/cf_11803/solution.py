"""
QUESTION:
Create a function `scientific_calculator(equation, decimal_places)` that takes a string `equation` representing a mathematical equation and an integer `decimal_places` as input, and returns the result of the equation rounded to the specified decimal places. The equation can contain addition, subtraction, multiplication, division, sine, cosine, square root, and exponentiation, as well as parentheses to prioritize the order of operations. The equation may include positive and negative numbers and decimal values.
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