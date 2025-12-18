"""
QUESTION:
Implement a function `median(l)` that calculates the median of a list of elements `l` without using built-in sorting functions or sorting the list. The function should handle lists with both even and odd numbers of elements, as well as lists with duplicate elements. The function should return `None` if the input list is empty.
"""

def median(lst):
    """Returns the median of the elements in the list lst, without sorting it or using built-in functions.
    Handles types with even and odd numbers of elements, as well as duplicate elements."""
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:    
        return find_kth_smallest(lst, n // 2)
    else:
        return ( find_kth_smallest(lst, n // 2 - 1) + find_kth_smallest(lst, n // 2) ) / 2.0

def find_kth_smallest(lst, k):
    if lst:
        pivot = lst[0]
        smaller_list = [x for x in lst if x < pivot]
        bigger_list = [x for x in lst if x > pivot]
        equal_list = [x for x in lst if x == pivot]
        m = len(smaller_list)
        n = len(equal_list)
        if k < m:
            return find_kth_smallest(smaller_list, k)
        elif k < m + n:
            return equal_list[0]
        else:
            return find_kth_smallest(bigger_list, k - m - n)