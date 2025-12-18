"""
QUESTION:
Create a function called `power` that calculates the power of a number raised to the nth power. The function should handle both positive and negative integers and return the power with alternating signs for negative bases. It should return `None` for non-integer bases or exponents. The function should have a time complexity of O(log n) and handle large values without causing a memory overflow. The function should take two parameters, `base` and `exponent`, both of which are integers.
"""

def power(base, exponent):
    # Check if base or exponent is non-integer
    if not isinstance(base, int) or not isinstance(exponent, int):
        return None
    
    # Check if base is negative
    if base < 0:
        if exponent % 2 == 0:
            return power(abs(base), exponent)
        else:
            return -1 * power(abs(base), exponent)
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Divide exponent by 2 and recursively calculate power
    temp = power(base, exponent // 2)
    
    # Multiply power by itself
    if exponent % 2 == 0:
        return temp * temp
    else:
        return base * temp * temp