"""
QUESTION:
Given a list of n elements, where n is between 1 and 10^6, write a function find_median(lst) that calculates the median element. The list should be sorted first, and if the length of the list is even, the median should be the average of the two middle elements; if the length of the list is odd, the median should be the middle element. The function should return the calculated median. Note that the function should use integer division to correctly calculate the index of the median.
"""

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        median = sorted_lst[n//2]
    return median