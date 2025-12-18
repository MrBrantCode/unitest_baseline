"""
QUESTION:
Construct a function `three_input_AND_using_NAND(A, B, C)` that implements a three-input AND gate using only two-input NAND gates. The function should take three inputs A, B, and C and return the result of the AND operation. The solution should use the least amount of gates possible.
"""

def NAND(A, B):
    return not (A and B)

def AND_using_NAND(A, B):
    temp = NAND(A, B)
    return NAND(temp, temp)

def three_input_AND_using_NAND(A, B, C):
    temp = AND_using_NAND(A, B)
    return AND_using_NAND(temp, C)