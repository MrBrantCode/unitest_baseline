"""
QUESTION:
Create a function `find_pivot(lst)` that takes a list of integers `lst` as input and returns the index of a "pivot" element. A pivot element is defined as an element where the sum of all elements to the left is equal to the mean of the elements to the right. If no such index is found, the function should return -1.
"""

def find_pivot(lst):
    # traversing list from left to right
    for i in range(len(lst)):
        # if sum of elements before the index is equal to the mean of elements after index
        if sum(lst[:i]) == sum(lst[i+1:])/(len(lst)-i-1) if (len(lst)-i-1) != 0 else 0:
            # return the index
            return i
    # if no such index is found
    return -1 