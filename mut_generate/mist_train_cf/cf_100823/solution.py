"""
QUESTION:
Write a function `max_value(num1, num2)` that takes two integers as inputs and returns the maximum value after performing operations based on the parity and sign of the inputs. The function should handle floating-point numbers and return an error message if either input is not a number. The operations are as follows: 
- If both integers are even, divide both by 2 and compare the results.
- If both integers are odd, multiply both by 3 and add 1, then compare the results.
- If one integer is even and the other is odd, subtract the smaller integer from the larger integer and compare the results.
- If both integers are negative, take the absolute value of both and compare the results.
- If both integers are positive, add the square root of the smaller integer to the larger integer and compare the results.
"""

import math
def max_value(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num1 < 0 and num2 < 0:
            return max(abs(num1), abs(num2))
        elif num1 % 2 == 0 and num2 % 2 == 0:
            return max(num1/2, num2/2)
        elif num1 % 2 != 0 and num2 % 2 != 0:
            return max(num1*3 + 1, num2*3 + 1)
        elif num1 > 0 and num2 > 0:
            return max(num1 + math.sqrt(min(num1, num2)), num2 + math.sqrt(min(num1, num2)))
        else:
            return abs(num1 - num2)
    else:
        return "Error: Inputs must be numbers."