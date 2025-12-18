"""
QUESTION:
Create a Python function named `fix_zeros` that takes a list as input, and moves all occurrences of the integer zero to the end of the list while maintaining the order of non-zero elements. The function should be able to handle lists of any depth (i.e., lists nested within lists), and should work with lists containing multiple data types (integers, strings, floats, etc.). The function should not use any pre-existing Python functions or libraries to directly solve the problem. If the input list does not contain any zeros, the function should return the original list.
"""

def fix_zeros(arr):
    non_zeros = []
    zeros = []
    for i in arr:
        if type(i) is list:
            non_zeros.append(fix_zeros(i))
        elif i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    return non_zeros + zeros