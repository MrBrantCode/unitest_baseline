"""
QUESTION:
Write a function `check_number` that takes an integer `n` as input and returns a string indicating its properties. The function should return "positive" if `n` is a positive even number, "negative" if `n` is a negative odd number, "zero" if `n` is 0, and "unknown" for all other cases.
"""

def check_number(n):
    if n > 0 and n % 2 == 0:
        return "positive"
    elif n < 0 and n % 2 != 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "unknown"