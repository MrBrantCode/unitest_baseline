"""
QUESTION:
Construct a Python function `move_zeros_to_end` that takes an array as input and repositions all instances of the integer zero to the terminal position of the array while preserving the sequential arrangement of the non-zero elements. The function should be capable of handling arrays embedded within arrays and relocate all instances of zero in these nested arrays to the terminal position of their individual arrays. The function should not use any pre-existing Python functions or libraries to directly address the problem.
"""

def move_zeros_to_end(array):
    if isinstance(array, list):
        return [move_zeros_to_end(i) for i in array if isinstance(i, list)] + [i for i in array if not isinstance(i, list) and i!=0] + [i for i in array if not isinstance(i, list) and i==0]
    else:
        return array