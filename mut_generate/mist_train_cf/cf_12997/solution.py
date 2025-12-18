"""
QUESTION:
Implement a function `getSum(a, b)` that returns the sum of two integers `a` and `b` without using the '+' operator. The function should use bit manipulation to achieve the addition logic. The input integers can be positive, negative, or zero, and the function should be able to handle any possible combination of inputs.
"""

def getSum(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Carry holds the common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b
        
        # Carry is left-shifted by 1 so that adding it to a gives the required sum
        b = carry << 1
    
    return a