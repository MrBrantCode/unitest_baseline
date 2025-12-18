"""
QUESTION:
Implement the function `add(x, y)` that takes two integer arguments and returns their sum without using any arithmetic operators or built-in functions for addition. The function should handle negative numbers and large numbers efficiently with a time complexity of O(1) and constant memory usage, regardless of the input size.
"""

def add(x, y):
    # XOR operation to find the sum without carrying
    sum_without_carry = x ^ y
    
    # AND operation followed by a left shift to find the carry
    carry = (x & y) << 1
    
    # Repeat the process until there is no carry left
    while carry != 0:
        # Update x with the sum without carry
        x = sum_without_carry
        
        # Update y with the carry
        y = carry
        
        # XOR operation to find the new sum without carrying
        sum_without_carry = x ^ y
        
        # AND operation followed by a left shift to find the new carry
        carry = (x & y) << 1
    
    # Return the final sum
    return sum_without_carry