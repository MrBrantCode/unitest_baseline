"""
QUESTION:
Write a function, `count_parameters`, that accepts a variable number of arguments and returns the total count of parameters passed. The function should have a maximum of 5 parameters. Do not use any built-in functions, libraries, or loops to count the parameters.
"""

def count_parameters(a=None, b=None, c=None, d=None, e=None):
    parameters = [a, b, c, d, e]
    count = 0
    while parameters:
        if parameters.pop(0) is not None:
            count += 1
    return count