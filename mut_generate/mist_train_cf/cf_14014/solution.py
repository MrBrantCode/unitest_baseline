"""
QUESTION:
Write a function `find_larger_num(num1, num2)` that returns the larger number from two given numbers. The function should handle cases where the numbers are equal, negative, or floating-point numbers. If the numbers are equal, return "Both numbers are equal." If both numbers are negative, return the one closer to zero.
"""

def find_larger_num(num1, num2):
    if num1 == num2:
        return "Both numbers are equal."
    elif num1 < 0 and num2 < 0:
        if abs(num1) < abs(num2):
            return num1
        else:
            return num2
    elif num1 < 0 or num2 < 0:
        if abs(num1) > abs(num2):
            return num1
        else:
            return num2
    elif isinstance(num1, float) or isinstance(num2, float):
        if isinstance(num1, int):
            num1 = float(num1)
        if isinstance(num2, int):
            num2 = float(num2)
        if num1 > num2:
            return num1
        else:
            return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2