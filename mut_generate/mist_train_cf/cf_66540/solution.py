"""
QUESTION:
Create a function named `find_hcf_lcm` that calculates the highest common factor (HCF) and the least common multiple (LCM) of two numbers. The function should take two integers as input and return their HCF and LCM. Use the math module's gcd function to calculate the HCF and the mathematical relation LCM(a, b) = |a*b| / HCF(a, b) to calculate the LCM.
"""

import math

def find_hcf_lcm(num1, num2):
    """
    Calculate the highest common factor (HCF) and the least common multiple (LCM) of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        tuple: A tuple containing the HCF and LCM of the two numbers.
    """
    hcf = math.gcd(num1, num2)
    lcm = abs(num1 * num2) // hcf
    return hcf, lcm