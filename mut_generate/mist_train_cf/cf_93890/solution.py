"""
QUESTION:
Create a function called `divide_numbers` that takes two parameters, `x` and `y`. The function should return the result of the division of `x` by `y`. However, if `x` and `y` are equal, the function should return the custom error message "Error: x and y are equal". If `y` is zero, the function should return the custom error message "Error: Cannot divide by zero".
"""

def divide_numbers(x, y):
    if x == y:
        return "Error: x and y are equal"
    
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    
    return result