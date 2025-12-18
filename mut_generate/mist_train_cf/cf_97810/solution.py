"""
QUESTION:
Write a function named `sum_of_squares` that takes two integers `x` and `y` as input, returns the sum of their squares, and prints "Test Passed" if the following conditions are met: `x` is odd and greater than or equal to 3, `y` is even and less than or equal to 10, and the sum of their squares is greater than 100. If these conditions are not met, the function should return `None`.
"""

def sum_of_squares(x, y):
    if x >= 3 and x % 2 != 0 and y <= 10 and y % 2 == 0:
        sum_squares = x**2 + y**2
        if sum_squares > 100:
            print("Test Passed")
            return sum_squares
    return None