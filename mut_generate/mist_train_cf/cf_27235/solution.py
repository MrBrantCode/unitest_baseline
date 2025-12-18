"""
QUESTION:
Implement a function `circularShift` that takes a 2D array `psf` and its size `psfSize` as input. The function should perform a circular shift operation on the 2D array such that its center is moved to the coordinate (0,0) and return the resulting circularly shifted 2D array. The circular shift operation involves shifting the elements of the array in a circular manner. The input 2D array is a square matrix with equal number of rows and columns. The size of the 2D array is passed as the `psfSize` parameter.
"""

from typing import List

def circularShift(psf: List[List[int]], psfSize: int) -> List[List[int]]:
    shift = -(psfSize // 2)
    shifted_psf = [row[-shift:] + row[:-shift] for row in psf[-shift:] + psf[:-shift]]
    return shifted_psf