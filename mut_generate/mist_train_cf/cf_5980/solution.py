"""
QUESTION:
Create a function named `solve_linear_equation` that takes two non-zero integers `a` and `b` as parameters and solves the linear equation `ax + b = 0`. The function should first check if `a` is zero and output a message if it is. If `a` is not zero, it should then check if `b` is zero and output the value of `x` if it is. If both `a` and `b` are non-zero, the function should calculate the value of `x` using the formula `x = -b/a` and output the value of `x` rounded to two decimal places. The function should also check if the result of `x` is a whole number and output a message if it is not, and check if the absolute value of `x` is less than or equal to 100 and output a message if it is not.
"""

def solve_linear_equation(a, b):
    if a == 0:
        return "The equation is not linear."
    elif b == 0:
        return "The value of x is 0."
    else:
        x = -b / a
        if x % 1 != 0:
            return "The solution is not an integer."
        elif abs(x) > 100:
            return "The solution is out of range."
        else:
            return f"The value of x is {x:.2f}."