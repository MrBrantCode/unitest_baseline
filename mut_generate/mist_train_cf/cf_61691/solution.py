"""
QUESTION:
Write a function `elite_truncation(figure, low, apex)` that takes a string `figure` representing a numerical value and two integers `low` and `apex` as input, and returns the integer closest to `figure` without using the `round()` function. The function should validate that `figure` represents a valid integer or float within the range `[low, apex]`. If `figure` is equidistant from two integers, the function should round towards zero. If `figure` is not a valid number or is out of range, return an error message.
"""

def elite_truncation(figure, low, apex):
    try:
        number = float(figure)
    except ValueError:
        return "Error: Invalid input."
    
    if number < low or number > apex:
        return "Error: Out of range."
    
    integer_part = int(number)
    fractional_part = abs(number - integer_part)

    if fractional_part < 0.5:
        return integer_part
    elif fractional_part == 0.5:
        # Direct rounding towards zero
        return integer_part if integer_part > 0 else integer_part - 1
    else:
        # If figure is positive, add 1; if figure is negative, subtract 1
        return integer_part + 1 if integer_part > 0 else integer_part - 1