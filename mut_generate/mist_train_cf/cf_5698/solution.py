"""
QUESTION:
Create a function named `subtract_and_check_prime` that takes two integer arguments `num1` and `num2`. The function should subtract `num2` from `num1` and return the result. However, if `num2` is greater than `num1` or if either `num1` or `num2` is negative, the function should return an error message. Additionally, if the result is a prime number, it should be returned as a positive number; otherwise, it should be returned as a negative number. Assume the input numbers will not exceed the range of a 32-bit signed integer.
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