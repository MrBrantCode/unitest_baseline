"""
QUESTION:
Determine the second integer given the least common multiple (LCM) and greatest common divisor (GCD) of two integers. 

Function name: find_second_integer

Given information:
- The LCM of the two integers is 240.
- The GCD of the two integers is 24.
- One of the integers is 48.

Restrictions:
- Use the relationship that the product of LCM and GCD equals the product of the integers.
"""

def find_second_integer(LCM, GCD, integer1):
    """
    This function calculates the second integer given the least common multiple (LCM) and 
    greatest common divisor (GCD) of two integers and one of the integers.
    
    Args:
        LCM (int): The least common multiple of the two integers.
        GCD (int): The greatest common divisor of the two integers.
        integer1 (int): One of the integers.

    Returns:
        int: The second integer.
    """
    return (LCM * GCD) // integer1