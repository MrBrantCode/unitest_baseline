"""
QUESTION:
Write a function `find_intersection(list_one, list_two)` that finds the intersection of two given arrays, defined as the common elements between the two arrays in the order they appear in the first array. Assume that the given arrays do not contain any duplicate elements. Do not use any built-in intersection functions or sets.
"""

def find_intersection(list_one, list_two):
    intersection = []
    for num in list_one:
        if num in list_two:
            intersection.append(num)
    return intersection