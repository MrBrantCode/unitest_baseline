"""
QUESTION:
Write a function `divide_numbers` that takes two integers `x` and `y` as input and returns their division result. The division should be performed using both floating point and integer division. If the inputs do not cause any division by zero errors, return the results as a tuple of two values. However, if the inputs cause a division by zero error, return a tuple with a meaningful error message instead. Assume that the inputs will always be integers.
"""

def divide_numbers(x, y):
    try:
        return (x / y, x // y)
    except ZeroDivisionError:
        return ("Error: Division by zero is not allowed", "Error: Division by zero is not allowed")