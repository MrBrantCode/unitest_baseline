"""
QUESTION:
Create a function named `solve_linear_equation` that takes two parameters `a` and `b`, both non-zero integers, and solves the linear equation ax + b = 0. If `a` is zero, return a message stating the equation is not linear. If `b` is zero, return the value of x as 0. If both `a` and `b` are non-zero, calculate the value of x using the formula x = -b/a and return its value rounded to two decimal places. Additionally, check if the result of x is a whole number and return a message stating the solution is not an integer if it's not. Also, check if the absolute value of x is less than or equal to 100, and return a message stating the solution is out of range if it's not.
"""

def solve_linear_equation(a, b):
    if a == 0:
        return "The equation is not linear."
    elif b == 0:
        x = 0
        result = f"The value of x is {x:.2f}."
        if x % 1 != 0:
            result += "\nThe solution is not an integer."
        if abs(x) > 100:
            result += "\nThe solution is out of range."
        return result
    else:
        x = -b/a
        result = f"The value of x is {x:.2f}."
        if x % 1 != 0:
            result += "\nThe solution is not an integer."
        if abs(x) > 100:
            result += "\nThe solution is out of range."
        return result