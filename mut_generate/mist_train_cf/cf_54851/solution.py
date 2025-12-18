"""
QUESTION:
Create a function `area_trapezoid` that calculates the area of a trapezoid given its dimensions: base1, base2, and height. The area should be calculated with a precision of up to 2 decimal places using the formula: Area = ((base1 + base2) / 2) * height. The function should also include error handling to check if the given dimensions are within the constraints: base1, base2, and height must be real numbers between 1 and 10^5 (inclusive). If the dimensions are out of constraints or invalid, the function should return an error message.
"""

def area_trapezoid(base1, base2, height):
    # Error handling for invalid cases
    if type(base1) not in [int, float] or type(base2) not in [int, float] or type(height) not in [int, float]:
        return "Error: Arguments must be numbers"
    elif base1 <= 0 or base2 <= 0 or height <= 0:
        return "Error: Dimensions must be greater than 0"
    elif base1 > 10**5 or base2 > 10**5 or height > 10**5:
        return "Error: Dimensions must be less than or equal to 100000 (10^5)"
    # Calculate area
    else:
        area = ((base1 + base2) / 2) * height
        return round(area, 2)