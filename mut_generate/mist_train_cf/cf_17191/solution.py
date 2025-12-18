"""
QUESTION:
Write a function named `find_intersection` that takes two arrays of integers as input and returns a new array containing the intersection of the two input arrays. The order of the elements in the output array does not matter. You cannot use built-in array methods or functions such as `filter()`, `includes()`, or `reduce()`. The input arrays can have any number of elements and will only contain integers.
"""

def find_intersection(array1, array2):
    intersection = []
    for num in array1:
        if num in array2 and num not in intersection:
            intersection.append(num)
    return intersection