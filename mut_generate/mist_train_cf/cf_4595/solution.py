"""
QUESTION:
Write a function named `compute_modulo(num1, num2)` that takes two positive integers `num1` and `num2` between 1 and 1000 inclusive as input, where `num2` is not equal to 1 and not greater than `num1`. The function should return the modulo of `num1` and `num2` and indicate whether `num1` is divisible by `num2`.
"""

def compute_modulo(num1, num2):
    if num2 == 1 or num2 > num1:
        return "Error: The second number must be greater than 1 and not greater than the first number."

    modulo = num1 % num2
    result = f"The modulo of {num1} and {num2} is {modulo}."

    if num1 % num2 == 0:
        result += f" {num1} is divisible by {num2}."
    else:
        result += f" {num1} is not divisible by {num2}."
    return result