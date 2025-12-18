"""
QUESTION:
Write a function named `SumNestedArray` that takes a nested array of integers as input and returns the total sum of all integers in the array, regardless of the depth of nesting. The function should be able to handle arrays that contain other arrays, not just direct integers.
"""

def SumNestedArray(nestedArray):
    sum = 0
    for item in nestedArray:
        if isinstance(item, list):
            sum += SumNestedArray(item)
        else:
            sum += item
    return sum