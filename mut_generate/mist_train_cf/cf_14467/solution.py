"""
QUESTION:
Create a function named `find_sum` that takes four parameters. The function should add all four parameters together and return the result. If any of the parameters are non-numeric, the function should return an error message "Invalid input. Please provide valid numeric values for all parameters."
"""

def find_sum(x, y, z, a):
    try:
        result = x + y + z + a
        return result
    except TypeError:
        return "Invalid input. Please provide valid numeric values for all parameters."