"""
QUESTION:
Create a function `check_irregularities(data)` that takes a linear array of integers `data` as input and returns "yes" if the differences between consecutive elements in the array are not uniform, and "no" otherwise. The array is guaranteed to have at least two elements.
"""

def check_irregularities(data):
    diffs = [j-i for i, j in zip(data[:-1], data[1:])]
    if len(set(diffs))>1:
        return "yes"
    else:
        return "no"