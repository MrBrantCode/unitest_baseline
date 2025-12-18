"""
QUESTION:
Design a function `multiplier` that multiplies two 4-bit binary numbers. The function should take two 4-bit binary numbers `A` and `B` as input and return the 8-bit product. The function should be designed using basic digital logic components, including multiplexers and adders.
"""

def multiplier(A, B):
    """
    This function multiplies two 4-bit binary numbers A and B and returns the 8-bit product.
    
    Parameters:
    A (int): A 4-bit binary number
    B (int): A 4-bit binary number
    
    Returns:
    int: The 8-bit product of A and B
    """
    # Convert the input integers to binary and remove the '0b' prefix
    bin_A = bin(A)[2:].zfill(4)
    bin_B = bin(B)[2:].zfill(4)
    
    # Initialize the product to 0
    product = 0
    
    # Iterate over each bit in B
    for i, bit in enumerate(reversed(bin_B)):
        # If the current bit is 1, add the corresponding shifted value of A to the product
        if bit == '1':
            product += int(bin_A, 2) << i
    
    # Return the 8-bit product
    return product & 0xFF  # Mask the product to 8 bits