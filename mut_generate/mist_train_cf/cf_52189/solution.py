"""
QUESTION:
Write a function `minDominoRotations` that takes two lists of integers `A` and `B` of the same length as input, and returns the minimum number of rotations needed to make all elements in either list `A` or list `B` equal to a specific element. If no such rotations are possible, return -1. Additionally, write a function `canBeEqual` that checks whether such rotations are possible for lists `A` and `B`.
"""

def minDominoRotations(A, B):
    def check(x):
        """
        Return minimum number of swaps 
        if one could make all elements in A or B equal to x.
        Else return -1.
        """
        rotations_a = rotations_b = 0
        for i in range(len(A)):
            if A[i] != x and B[i] != x:
                return -1
            elif A[i] != x:
                rotations_a += 1
            elif B[i] != x:
                rotations_b += 1
        return min(rotations_a, rotations_b)

    rotations = check(A[0]) 
    if rotations != -1 or A[0] == B[0]:
        return rotations 
    else:
        return check(B[0])