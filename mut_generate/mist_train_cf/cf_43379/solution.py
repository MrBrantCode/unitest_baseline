"""
QUESTION:
Write a function called sum_of_digits that takes a non-negative integer as the first argument, and two optional arguments. If the second argument is provided, it should be an integer and the function returns the sum of the digits of the first argument raised to the power of the second argument. If the third argument is provided, it should be a non-zero integer and the function returns the result from the previous operation modulo the third argument. If the second or third arguments are not provided, the function should behave as if the previous operation was not applied. The function should return an error message if any of the arguments are invalid.
"""

def sum_of_digits(num, pow_val=None, mod_val=None):
    # Validate input
    if type(num) != int or num < 0:
        return 'Error: First argument must be a non-negative integer'

    # Calculate sum of digits
    sum_val = sum([int(digit) for digit in str(num)])

    # If second argument provided, raise sum to the power of second argument
    if pow_val is not None:
        if type(pow_val) != int:
            return 'Error: Second argument must be an integer'
        elif pow_val < 0:
            return 'Error: Second argument cannot be negative'

        sum_val = pow(sum_val, pow_val)

    # If third argument provided, calculate sum modulo third argument
    if mod_val is not None:
        if type(mod_val) != int:
            return 'Error: Third argument must be an integer'
        elif mod_val == 0:
            return 'Error: Third argument cannot be zero'

        sum_val = sum_val % mod_val

    return sum_val