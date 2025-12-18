"""
QUESTION:
Write a function named `zero_one_ratio` that calculates the ratio of zeroes to ones in the binary representation of a given positive integer. If the number of ones is zero, the function should return a special value to indicate that the ratio cannot be calculated. The function should work for any positive integer input.
"""

def zero_one_ratio(n):
    # converts the number to binary and then to string
    binary = str(bin(n)[2:])
    
    # counts the number of zeroes and ones
    zeroes = binary.count('0')
    ones = binary.count('1')
    
    # handles division by zero error
    if ones == 0:
        return None      # or return whatever you want

    # calculates and returns the ratio
    return zeroes / ones