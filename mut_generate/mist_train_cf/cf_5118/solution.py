"""
QUESTION:
Write a function `base_2_logarithm(n)` that calculates the base-2 logarithm of a given positive integer `n` using only bitwise operations. The function should handle cases where `n` is not a power of 2. The input `n` is guaranteed to be greater than 0.
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
    
    # Return the count minus 1, since the problem requires the actual base-2 logarithm
    return count - 1