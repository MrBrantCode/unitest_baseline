"""
QUESTION:
Write a function named `find_median` that takes a list of integers as input, sorts the list, and returns the median value. The function should handle both lists with an odd number of elements, where the median is the middle element, and lists with an even number of elements, where the median is the average of the two middle elements.
"""

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2:
        return sorted_lst[n//2]
    else:
        return sum(sorted_lst[n//2-1:n//2+1]) / 2.0