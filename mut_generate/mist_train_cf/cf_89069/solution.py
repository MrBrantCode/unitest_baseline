"""
QUESTION:
Create a function `subtract_and_check_prime(num1, num2)` that takes two integer arguments, `num1` and `num2`, and returns their difference if certain conditions are met. The function should return an error message if either argument is negative or if `num2` is greater than `num1`. Otherwise, it should return the difference as a negative number if it is not prime, and as a positive number if it is prime. Assume that the input numbers will not exceed the range of a 32-bit signed integer.
"""

def subtract_and_check_prime(num1, num2):
    if num1 < 0 or num2 < 0:
        return "Error: Arguments cannot be negative."
    if num2 > num1:
        return "Error: Second argument cannot be greater than the first argument."

    result = num1 - num2
    if result <= 1:
        return result

    for i in range(2, int(result**0.5) + 1):
        if result % i == 0:
            return -result

    return result