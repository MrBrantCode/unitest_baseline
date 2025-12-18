"""
QUESTION:
Implement `find_difference(a, b)` to calculate the absolute difference between two prime integers `a` and `b`, both within the range of -1000 to 1000, and round the result to the nearest whole number. The function should return an error message if `a` or `b` is outside the specified range or is not a prime number.
"""

import math

def find_difference(a, b):
    if a < -1000 or a > 1000 or b < -1000 or b > 1000:
        return "Integers must be within the range of -1000 to 1000"
    
    for i in range(2, int(math.sqrt(abs(a))) + 1):
        if a % i == 0:
            return "Integers must be prime numbers"
    for i in range(2, int(math.sqrt(abs(b))) + 1):
        if b % i == 0:
            return "Integers must be prime numbers"
    if a == 1 or b == 1:
        return "Integers must be prime numbers"
    
    difference = abs(a - b)
    rounded_difference = round(difference)
    return rounded_difference