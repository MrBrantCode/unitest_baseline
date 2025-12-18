"""
QUESTION:
Implement a function `calculate_exponent(num, base, exp)` that calculates the exponent such that the absolute difference between `num` and `base` raised to the power of `exp` is minimized. The function takes three parameters: `num` (an integer representing the number), `base` (an integer representing the base), and `exp` (an integer representing the initial exponent). The function should return the exponent that results in the minimum absolute difference.
"""

def calculate_exponent(num, base, exp):
    min_diff = abs(num - base**exp)  # Initialize minimum difference with the current exponent
    result_exp = exp  # Initialize the result exponent with the current value

    for i in range(exp - 1, 0, -1):  # Iterate from exp-1 to 1
        diff = abs(num - base**i)  # Calculate the absolute difference
        if diff < min_diff:  # If the difference is smaller than the current minimum difference
            min_diff = diff  # Update the minimum difference
            result_exp = i  # Update the result exponent

    return result_exp  # Return the exponent that minimizes the absolute difference