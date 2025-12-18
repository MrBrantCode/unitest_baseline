"""
QUESTION:
Write a function `calculate_side_length(n, m, align)` that calculates the side length of the 'm'th square in a sequence of squares constructed inside a square with side length 'n'. The sequence is constructed such that the diagonals of each inner square coincide with either the sides or the diagonals of the preceding square, depending on the boolean parameter 'align'. If 'align' is True, the new square aligns with the sides of the preceding square; otherwise, it aligns with the diagonals.
"""

import math

def entrance(n, m, align):
    for i in range(1, m):
        if align:
            n = n / math.sqrt(2)
            align = False
        else:
            n = n / 2
            align = True
    return n