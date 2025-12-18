"""
QUESTION:
Define a function named `classify_integer` that takes one argument, an integer `num`. The function should return a string indicating the classification of the integer as follows: "positive" if the integer is a positive even number, "negative" if it is a negative odd number, and "zero" if the integer is 0. If the input is not a numeric value or falls outside the range of -1000 to 1000 (inclusive), the function should return "unknown".
"""

def classify_integer(num):
    if not isinstance(num, int):
        return "unknown"
    elif num == 0:
        return "zero"
    elif num < -1000 or num > 1000:
        return "unknown"
    elif num > 0 and num % 2 == 0:
        return "positive"
    elif num < 0 and num % 2 != 0:
        return "negative"
    else:
        return "unknown"