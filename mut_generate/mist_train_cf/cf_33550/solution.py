"""
QUESTION:
Implement a function `find_median(lst)` that takes a list of integers as input and returns the median of the list. The median is the middle number when the list is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle numbers. The input list is not guaranteed to be sorted, so the function must sort the list before calculating the median.
"""

def find_median(lst):
    lst.sort()  
    n = len(lst)
    if n % 2 == 0:  
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (lst[mid1] + lst[mid2]) / 2  
    else:  
        median = lst[n // 2]  
    return median