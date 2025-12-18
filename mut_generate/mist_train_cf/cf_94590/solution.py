"""
QUESTION:
Implement a function `find_intersection(array1, array2)` that takes two arrays of integers as input and returns a new array containing the intersection of the two input arrays, without using built-in array methods or functions such as filter(), includes(), or reduce().
"""

def find_intersection(array1, array2):
    intersection = []
    for num in array1:
        if num in array2 and num not in intersection:
            intersection.append(num)
    return intersection