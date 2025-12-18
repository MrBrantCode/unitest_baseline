"""
QUESTION:
Create a function called `find_median` that takes a list of numbers as input and returns the median value. The list may contain repeated values and/or negative numbers. The function should handle both even and odd length lists, and for even length lists, it should return the arithmetic mean of the two middle numbers.
"""

def find_median(lst):
    lst.sort()  # sort the list
    n = len(lst)  # length of list
    
    # if length of list is even
    if n % 2 == 0:
        median1 = lst[n//2]  # fetching the n/2 th element
        median2 = lst[n//2 - 1]  # fetching the (n/2)th - 1 th element
        median = (median1 + median2)/2
    # if length of list is odd
    else:
        median = lst[n//2]
    return median