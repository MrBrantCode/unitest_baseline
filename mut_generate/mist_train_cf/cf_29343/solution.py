"""
QUESTION:
Implement the function `dumb_round(num: float) -> str` that takes a floating-point number `num` as input, rounds it to 2 decimal places, and returns the result as a string. If the number has no decimal places after rounding, the decimal point and trailing zeros should be removed from the string representation.
"""

def entrance(num: float) -> str:
    rounded_num = round(num, 2)  
    if rounded_num.is_integer():  
        return str(int(rounded_num))  
    else:
        return str(rounded_num)