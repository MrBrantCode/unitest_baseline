"""
QUESTION:
Create a function named `calculate_gcd_lcm` that calculates the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two non-negative integers. The function should also check whether these two integers fall within a specified range defined by a minimum and maximum value. If either or both of the integers are outside the range, return an error message. The function should not use built-in functions for calculating GCD or LCM. It should accept four parameters: two integers and the minimum and maximum values of the range, and return the GCD, LCM, or an error message as applicable.
"""

def calculate_gcd_lcm(int1, int2, min_value, max_value):
    """
    Calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two non-negative integers.
    
    Args:
    int1 (int): The first integer.
    int2 (int): The second integer.
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.
    
    Returns:
    tuple or str: A tuple containing the GCD and LCM if both integers are within the range, otherwise an error message.
    """

    # Check if integers are within the specified range
    if not (min_value <= int1 <= max_value and min_value <= int2 <= max_value):
        return "One or both of the integers are out of the specified range."

    # Calculate GCD
    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)

    # Calculate LCM using the formula: (a * b) / GCD
    lcm = (int1 * int2) // gcd(int1, int2)

    return (gcd(int1, int2), lcm)