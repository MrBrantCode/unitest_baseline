"""
QUESTION:
Write a function `special_rounding(value, low, high)` that takes a string or numeric value and two range-limit integers as input, and returns the closest integer to the input value without using built-in functions such as round(). The function should validate if the value entered is a valid integer or float, check if it's within the defined range, and handle complex and invalid cases by returning an error message. 

If the input value is equidistant from two integers, the function should round it towards zero and validate if the rounded integer falls within the range limits. If not, the function should automatically return the closest valid integer within the range. The function should return "Error: Invalid input." for non-numeric inputs and "Error: Out of range." for values outside the defined range.
"""

def entrance(value, low, high):
    # check if the value is a valid number
    try:
        val = float(value)
        l_bound = int(low)
        h_bound = int(high)
    except ValueError:
        return "Error: Invalid input."
    
    # check if the value is within the defined range
    if val < l_bound or val > h_bound:
        return "Error: Out of range."
    
    # special rounding to the nearest integer
    if val >= 0:
        if val - int(val) < 0.5 or int(val) + 1 > h_bound:
            rounded_val = int(val)
        else:
            rounded_val = int(val) + 1   
    else:
        if int(val) - val < 0.5 or int(val) - 1 < l_bound:
            rounded_val = int(val)
        else:
            rounded_val = int(val) - 1
            
    return rounded_val