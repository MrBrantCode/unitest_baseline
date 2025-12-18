"""
QUESTION:
Write a function `find_median` that takes a list of integers as input, and returns the median of the list. The function should handle cases where the list is empty, contains an even number of elements, or contains duplicate values. The median of a list with an even number of elements is the average of the two middle elements.
"""

def find_median(arr):
    if not arr:  
        return None

    arr.sort()  

    length = len(arr)
    mid_index = length // 2

    if length % 2 == 0:  
        return (arr[mid_index - 1] + arr[mid_index]) / 2.0

    return arr[mid_index]  