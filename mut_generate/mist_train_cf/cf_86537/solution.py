"""
QUESTION:
Implement a recursive function named `gcd_recursive` that calculates the greatest common divisor (GCD) of two integers `n1` and `n2` with a time complexity of O(log min(n1, n2)). The function should handle negative integers as input and not use any built-in functions or libraries to calculate the GCD.
"""

def gcd_recursive(n1, n2):
    # Convert negative integers to positive
    n1 = abs(n1)
    n2 = abs(n2)
    
    # Base case: if one of the numbers is 0, the other number is the GCD
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    
    # Recursive case: calculate the GCD using the Euclidean algorithm
    return gcd_recursive(n2 % n1, n1)