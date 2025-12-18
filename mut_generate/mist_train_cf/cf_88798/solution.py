"""
QUESTION:
Write a function `base_2_logarithm` that takes a positive integer `n` as input and returns its base-2 logarithm using only bitwise operations. The input integer `n` is greater than 0, and it may or may not be a power of 2.
"""

def base_2_logarithm(n):
    # Initialize the count
    count = 0
    
    # Keep shifting n to the right until it becomes 0
    while n:
        # Right shift n by 1 bit
        n >>= 1
        # Increment the count
        count += 1
    
    # Return the count
    return count - 1