"""
QUESTION:
Given an array of one's and zero's that represents a positive binary number convert the number to two's complement value.

Two's complement is the way most computers represent positive or negative integers. The most significant bit is negative. 

Examples:

-8 4 2 1 

[1,1,1,1] = -1

[1,0,0,0] = -8

[1,1,0,1] = -3

To get the two's complement negative notation of an integer, you take the number in binary. 

You then invert the digits, and add one to the result. 

For example:

[0,0,1,0] = 2 in base 10

[1,1,0,1] <- Flip the bits

   Add 1
   
[1,1,1,0] = -2

However, the arrays can have varying lengths, not just limited to 4.
"""

def convert_binary_to_twos_complement(binary):
    # Step 1: Find the first '1' from the right
    inverted = []
    found_one = False
    
    for bit in reversed(binary):
        if found_one:
            inverted.append(1 - bit)
        else:
            inverted.append(bit)
            if bit == 1:
                found_one = True
    
    # Step 2: Reverse the inverted list to get the correct order
    return list(reversed(inverted))