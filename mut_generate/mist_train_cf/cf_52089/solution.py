"""
QUESTION:
Write a function `validate_numeric(num)` that checks if a given string `num` consists solely of numerical values, including decimal values and negative numbers. The function should identify whether the sequence is an integer or a floating-point number and handle errors without interrupting the program. The validation should be case insensitive.
"""

def validate_numeric(num):
    try:
        if '.' in num:
            num = float(num)
            print("This is a float number.")
        else:
            num = int(num)
            print("This is an integer.")
        return True
    except ValueError:
        print("This is not a numeric value.")
        return False