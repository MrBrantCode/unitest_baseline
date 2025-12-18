"""
QUESTION:
Implement a function `binary_search_recursive(data, target, start, end, comparisons)` that performs a recursive binary search on a sorted list `data` to find the index of the first occurrence of `target`. The function should also return the number of comparisons made during the search process. The input list may contain duplicate elements and the function should handle this properly.
"""

def binary_search_recursive(data, target, start, end, comparisons):
    if start > end:
        return -1, comparisons
    
    mid = (start + end) // 2
    comparisons += 1
    
    if data[mid] == target:
        if mid > 0 and data[mid-1] == target:
            return binary_search_recursive(data, target, start, mid-1, comparisons)
        else:
            return mid, comparisons
    elif data[mid] > target:
        return binary_search_recursive(data, target, start, mid-1, comparisons)
    else:
        return binary_search_recursive(data, target, mid+1, end, comparisons)