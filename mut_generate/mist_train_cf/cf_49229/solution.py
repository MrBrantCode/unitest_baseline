"""
QUESTION:
Create a Python script with four functions: `add_numbers`, `exponentiation`, `modulus`, and `root`. The `add_numbers` function should take two numbers as input and return their sum. The `exponentiation` function should take a base and an exponent as input and return the result of the exponentiation operation. The `modulus` function should take a number and a divisor as input and return the remainder of the division operation. The `root` function should take a number and a root as input and return the result of the root extraction operation. The script should then execute these functions with specific parameters and print out the results.
"""

import math

def entance(num1, num2, base, exponent, num, divisor, n, root):
    sum_result = num1 + num2
    exponentiation_result = base ** exponent
    modulus_result = num % divisor
    root_result = n ** (1.0 / root)
    return sum_result, exponentiation_result, modulus_result, root_result