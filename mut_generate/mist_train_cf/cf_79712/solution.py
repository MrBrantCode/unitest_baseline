"""
QUESTION:
Write a function named `common_elements` that takes four arrays `a1`, `a2`, `a3`, `a4` as input. The function should return an array of elements that are common to all four input arrays and appear at the same index. The function should work with arrays of varying lengths, stopping at the length of the shortest array, and support different data types including integers, strings, and complex numbers.
"""

def common_elements(a1, a2, a3, a4):
    common = []
    for x1, x2, x3, x4 in zip(a1, a2, a3, a4):
        if x1 == x2 == x3 == x4:
            common.append(x1)
    return common