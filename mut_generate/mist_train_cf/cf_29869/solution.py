"""
QUESTION:
Write a Python function called `check_number` that takes an integer `num` as input and returns a string indicating whether the number is positive, negative, or zero. The function should return "Positive" if `num` is greater than 0, "Negative" if `num` is less than 0, and "Zero" otherwise.
"""

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"