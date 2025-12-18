"""
QUESTION:
Write a function called `multiply` that takes two integers `x` and `y` as input and returns their product without using the multiplication operator. The function should handle negative numbers and have a time complexity not exceeding O(N), where N is the magnitude of `y`.
"""

def multiply(x, y):
    result = 0

    # determine if y is negative
    y_is_negative = False
    if y < 0:
        y_is_negative = True
        y = -y

    # calculate the result
    for i in range(y):
        result += x

    # if y was negative, flip the sign of the result
    if y_is_negative:
        result = -result

    return result