"""
QUESTION:
Create a function `closest_integer(value)` that takes a string `value` representing a number and returns the closest integer to it without using built-in functions like `round()`. 

The function should validate if the given `value` is a valid float or integer. If not, return the error message "Error: Invalid input." If the number is equidistant from two integers, round it away from zero, meaning return the integer that is farthest from zero.
"""

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number and returns
    the closest integer to it, without using built-in functions like round(). Also,
    validate if the given value is a valid float or integer. If not, return an error
    message. If the number is equidistant from two integers, round it away from zero.

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    try:
        num = float(value)
        if num >= 0 and num - int(num) >= 0.5:
            return int(num) + 1
        elif num < 0 and int(num) - num >= 0.5:
            return int(num) - 1
        else:
            return int(num)
    except ValueError:
        return "Error: Invalid input."