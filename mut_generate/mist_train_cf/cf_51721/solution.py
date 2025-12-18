"""
QUESTION:
Design a function named `bit_flip` that takes two binary strings of equal length as input and returns a string describing whether the first binary string can be transformed into the second binary string by flipping exactly one bit. If possible, the function should return the position of the bit that needs to be flipped (using 1-indexing). If more than one bit needs to be flipped, the function should return "More than one bit needs flipping". If no bits need to be flipped, the function should return "No bit needs flipping".
"""

def bit_flip(binary1, binary2):
    flipped_bit = -1
    flip_counter = 0
    
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            flip_counter += 1
            flipped_bit = i + 1  # change this to 1-indexed
    
    if flip_counter > 1:
        return "More than one bit needs flipping"
    elif flip_counter == 1:
        return "Bit at position " + str(flipped_bit) + " needs to be flipped"
    else:
        return "No bit needs flipping"