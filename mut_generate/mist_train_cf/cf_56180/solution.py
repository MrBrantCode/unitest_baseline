"""
QUESTION:
Create a function named 'calculate_sum' that accepts two parameters. The function should return the sum of the two numbers if they are integers or floats. If the parameters are strings that can be converted into integers or floats, the function should convert these strings to corresponding integer or float values before proceeding with the summation. If any of the parameters cannot be converted to a number or are not numbers, the function should return 'None'. The function should also return 'None' if the number of parameters passed is not exactly two.
"""

def calculate_sum(param1, param2):
    if not isinstance(param1, (int, float, str)) or not isinstance(param2, (int, float, str)):
        return None

    try:
        return float(param1) + float(param2)
    except ValueError:
        return None