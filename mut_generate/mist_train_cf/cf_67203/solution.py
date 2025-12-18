"""
QUESTION:
Create a function `evaluate_divisibility(num, divisor)` that calculates how many times `num` can be divided by `divisor` before reaching a non-integer result. The function should only accept non-negative integers as input and should not allow division by zero. If the inputs do not meet these criteria, return an error message.
"""

def evaluate_divisibility(num, divisor):
    if type(num) != int or type(divisor) != int:
        return "Inputs must be integers."
    elif divisor == 0:
        return "Divisor cannot be zero."
    elif num < 0 or divisor < 0:
        return "Inputs cannot be negative."
    elif num < divisor:
        return 0
    else:
        count = 0
        while num % divisor == 0:
            num = num / divisor
            count += 1
        return count