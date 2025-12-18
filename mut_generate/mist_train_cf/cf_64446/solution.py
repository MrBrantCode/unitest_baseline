"""
QUESTION:
Write a function `median` that calculates the median of a list of numbers without sorting the list or using built-in functions. The function should handle lists with both even and odd numbers of elements, as well as duplicate elements. If the list is empty, the function should return `None`.
"""

def find_median(l):
    """Returns the median of the elements in the list l, without sorting it or using built-in functions. 
    Handles tuples with even and odd numbers of elements, as well as duplicate elements."""
    n = len(l)
    if n < 1:
            return None
    if n % 2 == 1:    
        return find_kth_smallest(l, n // 2)
    else:
        return ( find_kth_smallest(l, n // 2 - 1) + find_kth_smallest(l, n // 2) ) / 2.0

def find_kth_smallest(l, k):
    if l:
        pivot = l[0]
        smaller_list = [x for x in l if x < pivot]
        bigger_list = [x for x in l if x > pivot]
        equal_list = [x for x in l if x == pivot]
        m = len(smaller_list)
        n = len(equal_list)
        if k < m:
            return find_kth_smallest(smaller_list, k)
        elif k < m + n:
            return equal_list[0]
        else:
            return find_kth_smallest(bigger_list, k - m - n)