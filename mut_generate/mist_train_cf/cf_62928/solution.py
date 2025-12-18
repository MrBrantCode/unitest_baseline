"""
QUESTION:
Create a function `find_hcf_and_lcm` that takes three integers as input and returns a tuple containing the highest common factor (HCF) and the lowest common multiple (LCM) of the three numbers. The function should use the `math.gcd` function to calculate the HCF. For the LCM, it should either use the `math.lcm` function (available in Python 3.9 and later) or a custom implementation if `math.lcm` is not available.
"""

import math 

def find_hcf_and_lcm(num1, num2, num3):   
    """
    Calculate the highest common factor (HCF) and the lowest common multiple (LCM) of three numbers.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    tuple: A tuple containing the HCF and LCM of the three numbers.
    """
    # Calculate the HCF using math.gcd
    hcf = math.gcd(math.gcd(num1, num2), num3)
  
    # Check if math.lcm is available (Python 3.9 and later)
    if hasattr(math, 'lcm'):
        lcm = math.lcm(math.lcm(num1, num2), num3)
    else:
        # Custom implementation of LCM for lower Python versions
        def lcm(x, y):
            """
            Calculate the lowest common multiple of two numbers.

            Args:
            x (int): The first number.
            y (int): The second number.

            Returns:
            int: The LCM of the two numbers.
            """
            greater = max(x, y)
            while True:
                if greater % x == 0 and greater % y == 0:
                    return greater
                greater += 1

        lcm = lcm(lcm(num1, num2), num3)
      
    return hcf, lcm