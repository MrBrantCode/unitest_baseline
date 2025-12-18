"""
QUESTION:
Create a function named `digit_sum` that takes one to three arguments: a non-negative integer `n`, an optional power `power` with a default value of 1, and an optional modulus `mod` with a default value of `None`. The function should calculate and return the sum of the digits of `n`, optionally raised to the power of `power`, and optionally modulo `mod`. Handle edge cases where `power` is negative, `mod` is zero, and ensure the function can handle large integers and floating point numbers. If `n` is a string representation of a number, it should be converted to an integer before performing the calculations.
"""

def digit_sum(n, power=1, mod=None):
    # Convert input to integer if it's a string
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            return "Error: Input needs to be numerical"

    # Check if arguments are negative
    if n < 0 or power < 0:
        return "Error: Arguments cannot be negative"

    # Sum the digits
    digit_sum = sum(int(i) for i in str(n))
    
    # If mod is zero, return an error message
    if mod is not None and mod == 0:
        return "Error: Third argument (modulus) cannot be zero"

    # Raise to power
    res = pow(digit_sum, power)

    # Modulo if applicable
    if mod is not None:
        res %= mod

    # Round if power is a float
    res = round(res) if isinstance(power, float) else res

    return res