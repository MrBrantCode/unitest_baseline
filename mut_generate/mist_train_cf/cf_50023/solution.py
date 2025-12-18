"""
QUESTION:
Create a function named `find_lcm` that takes three integers `num1`, `num2`, and `num3` as input and returns their least common multiple (LCM). Use the concept of Greatest Common Divisor (GCD) to determine the LCM. The function should be efficient and able to handle any positive integer inputs.
"""

import math

def find_lcm(num1, num2, num3):
    # compute gcd of num1 and num2
    gcd = math.gcd(num1, num2)

    # compute lcm of num1 and num2
    lcm_num1_num2 = (num1*num2) // gcd

    # compute gcd of lcm_num1_num2 and num3
    gcd = math.gcd(lcm_num1_num2, num3)

    # compute lcm of three numbers
    lcm = (lcm_num1_num2*num3) // gcd

    return lcm