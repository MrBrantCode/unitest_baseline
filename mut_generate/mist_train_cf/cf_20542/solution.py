"""
QUESTION:
Design a function `multiply_without_operator` that takes two integers `a` and `b` as input and returns their product without using the multiplication operator. The function should have a time complexity of O(log N), where N is the larger of the two numbers, and a space complexity of O(1).
"""

def multiply_without_operator(a, b):
    """
    This function multiplies two integers without using the multiplication operator.
    
    It uses a binary multiplication algorithm, iterating through the bits of the smaller number,
    adding the larger number to the product for each set bit, and doubling the larger number in each iteration.
    
    The function has a time complexity of O(log N), where N is the larger of the two numbers,
    and a space complexity of O(1) because it only uses a single product variable for computation.
    """
    
    # Determine the larger and smaller numbers
    N = max(abs(a), abs(b))
    M = min(abs(a), abs(b))
    
    # Initialize the product variable to 0
    product = 0
    
    # Iterate through the bits of M from the least significant bit (LSB) to the most significant bit (MSB)
    while M > 0:
        # If the current bit of M is set (1), add N to the product variable
        if M & 1:
            product += N
        
        # Double the value of N
        N <<= 1
        
        # Shift the bits of M to the right by 1 position
        M >>= 1
    
    # Return the absolute value of the product, considering the signs of the input numbers
    return -product if (a < 0) ^ (b < 0) else product