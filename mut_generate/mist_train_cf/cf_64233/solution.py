"""
QUESTION:
Create a recursive function `calc_factorial` that takes an integer argument and returns the factorial of that number. The function should handle error cases for non-integer types, negative numbers, and large inputs (above 12) that may cause integer overflow.
"""

def entrance(n):
    try:
        n = int(n)
        if n < 0:
            return "Error: Cannot compute factorial for negative numbers"
        elif n == 0:
            return 1
        elif n > 12:
            return "Error: Computation of factorial for this number may cause integer overflow"
        else:
            return n * entrance(n - 1)
    except ValueError:
        return "Error: Please input an integer"