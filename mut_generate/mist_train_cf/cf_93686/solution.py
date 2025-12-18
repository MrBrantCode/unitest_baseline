"""
QUESTION:
Write a function `find_intersection` that takes two arrays `list_one` and `list_two` as input and returns their intersection, i.e., the common elements between the two arrays, in the order they appear in `list_one`. The function should not use any built-in intersection functions or sets. Assume the input arrays do not contain any duplicate elements and can contain negative numbers.
"""

def find_intersection(list_one, list_two):
    intersection = []
    
    for num in list_one:
        if num in list_two:
            intersection.append(num)
    
    return intersection