"""
QUESTION:
Design a function `find_intersection(list_one, list_two)` that takes two lists of integers as input and returns a list containing their intersection, defined as the common elements between the two lists, in the order they appear in `list_one`. You are not allowed to use any built-in intersection functions or sets. Assume the input lists do not contain any duplicate elements and can contain negative numbers.
"""

def find_intersection(list_one, list_two):
    intersection = []
    
    for num in list_one:
        if num in list_two:
            intersection.append(num)
    
    return intersection