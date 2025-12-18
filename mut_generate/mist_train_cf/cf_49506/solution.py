"""
QUESTION:
Create a function called `find_hcf_lcm` that takes two integers as input and returns their highest common factor (HCF) and smallest common multiple (LCM). The function should use the math module's `gcd` function to find the HCF. For the LCM, it should use the `lcm` function if available (Python 3.9 and later), otherwise, it should use the formula `abs(a*b) // math.gcd(a, b)`.
"""

import math

def find_hcf_lcm(a, b):
    """
    This function calculates the highest common factor (HCF) and 
    smallest common multiple (LCM) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing the HCF and LCM of the two integers.
    """
    # find highest common factor
    hcf = math.gcd(a, b)
    
    # find smallest common multiple
    lcm = math.lcm(a, b) if hasattr(math, 'lcm') else abs(a*b) // math.gcd(a, b)
    
    return hcf, lcm