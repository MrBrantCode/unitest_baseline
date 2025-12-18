"""
QUESTION:
Write a function `factorial(num)` that calculates the factorial of a given non-negative integer `num`. The function should return `1` for inputs `0` and `1`, and the product of all positive integers less than or equal to `num` for inputs greater than `1`. The function should handle input validation for negative numbers by printing an error message and returning `None`. The function should be optimized to handle large numbers efficiently, with a time complexity of O(n), where n is the input number.
"""

import math

def entance(num):
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        return math.prod(range(2, num+1))