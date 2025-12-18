"""
QUESTION:
Create a function called `harmonic_mean` that calculates the harmonic mean of three integers. The function should only accept three positive, non-zero integers as input. If any of the inputs are not integers or are not positive, the function should return an error message.
"""

def harmonic_mean(num1, num2, num3):
    if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
        if num1 > 0 and num2 > 0 and num3 > 0:
            return 3 / (1/num1 + 1/num2 + 1/num3)
        else:
            return "Error: All inputs must be positive, non-zero integers."
    else:
        return "Error: All inputs must be integers."