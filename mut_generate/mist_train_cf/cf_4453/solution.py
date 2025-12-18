"""
QUESTION:
Create a function `round_float` that takes a single integer as input. The function should return a float rounded to the nearest hundredth if the input is a positive integer greater than zero and within the range of 1 to 1000 (inclusive). If the input is outside of this range, return the string "Input out of range". If the input is negative or zero, return the string "Invalid input".
"""

def round_float(input):
    if input <= 0:
        return "Invalid input"
    elif input < 1 or input > 1000:
        return "Input out of range"
    else:
        return round(input, 2)