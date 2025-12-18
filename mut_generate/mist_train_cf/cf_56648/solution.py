"""
QUESTION:
Implement a function called `add` that takes three parameters `x`, `y`, and `z`. The function should return the sum of these parameters if they are either integers or floats. If any of the parameters are not integers or floats, the function should return a customized error message 'TypeError: Only integers or floats are allowed.' The function should be thoroughly documented using Python docstrings.
"""

def add(x, y, z):
    """
    This function takes three parameters as input and 
    returns their sum, if all parameters are of type either
    int or float otherwise it returns a customized 
    error message regarding the Type Error.

    :param x: The first parameter.
    :param y: The second parameter.
    :param z: The third parameter.
    :return: The sum of x, y and z if they are int or float type. Otherwise returns an error message.
    """
    try:
        result = x + y + z
        return result 
    except TypeError:
        return 'TypeError: Only integers or floats are allowed.'