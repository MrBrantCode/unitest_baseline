"""
QUESTION:
Implement the root static method for NaturalNumber using the interval halving root algorithm. The method should take a NaturalNumber object 'n' and an optional 'tolerance' parameter (default is 10^-8), and return the square root of 'n' within the given tolerance. Ensure the space complexity is O(1).
"""

def root(n, tolerance=10**-8):
    left = 0
    right = n
    while right - left > tolerance:
        mid = (left + right) / 2
        if mid ** 2 <= n:
            left = mid
        else:
            right = mid
    return (left + right) / 2