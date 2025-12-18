"""
QUESTION:
Create a function named `highest_common_factor` that takes two distinct positive integers `A` and `B` within the range of 1 to 100 as input and returns their highest common factor.
"""

def highest_common_factor(A, B):
    """
    This function calculates the highest common factor of two distinct positive integers A and B.
    
    Parameters:
    A (int): The first positive integer.
    B (int): The second positive integer.
    
    Returns:
    int: The highest common factor of A and B.
    """
    
    # Initialize the variable to store the highest common factor
    hcf = 1
    
    # Iterate from 1 to the smaller number
    for i in range(1, min(A, B) + 1):
        # Check if i is a factor of both A and B
        if A % i == 0 and B % i == 0:
            # Update the highest common factor
            hcf = i
    
    return hcf