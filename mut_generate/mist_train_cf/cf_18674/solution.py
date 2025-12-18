"""
QUESTION:
Create a function `round_to_nearest_multiple(num, decimal_place=0)` that takes in a number `num` and an optional argument `decimal_place` (default is 0), and returns the number rounded to the nearest multiple of 10, with the option to round to a specified decimal place.
"""

def round_to_nearest_multiple(num, decimal_place=0):
    # Step 1: Multiply the number by 10^decimal_place to shift the decimal place
    num *= 10**decimal_place
    
    # Step 2: Round the shifted number to the nearest whole number
    rounded_num = round(num)
    
    # Step 3: Divide the rounded number by 10^decimal_place to shift the decimal place back
    rounded_num /= 10**decimal_place
    
    # Step 4: Round the shifted number to the nearest multiple of 10
    rounded_multiple = round(rounded_num / 10) * 10
    
    return rounded_multiple