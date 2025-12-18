"""
QUESTION:
Write a function `relocate_zeroes(data)` that takes a list as input, moves all instances of zero to the end of the list while preserving the original sequence of non-zero elements, and handles nested lists in the same manner. The function should not use any pre-existing Python functions or libraries to directly address the problem.
"""

def relocate_zeroes(data):
    if not isinstance(data, list):
        return data
    else:
        res = [relocate_zeroes(i) if isinstance(i, list) else i for i in data]
        non_zeroes = [i for i in res if i != 0]
        zeroes = [i for i in res if i == 0]
        return non_zeroes + zeroes