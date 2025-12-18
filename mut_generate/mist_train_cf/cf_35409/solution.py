"""
QUESTION:
Insert bits of M into N such that M starts at bit j and ends at bit i. Given two 32-bit numbers N and M, and two integer indices i and j, write a function insertBits(N, M, i, j) that returns the modified N with M inserted into it. Assume that there are enough bits to fit M into N.
"""

def insertBits(N, M, i, j):
    # Create a mask to clear bits i through j in N
    allOnes = ~0
    left = allOnes << (j + 1)
    right = (1 << i) - 1
    mask = left | right

    # Clear bits i through j in N
    clearedN = N & mask

    # Shift M so that it lines up with bits i through j
    shiftedM = M << i

    # Merge M into N
    result = clearedN | shiftedM

    return result