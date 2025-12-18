"""
QUESTION:
Implement a recursive binary search function `binary_search` that takes in a sorted dataset and a search number, and returns the range of indices where the search number appears in the dataset. If the search number appears only once, return a range with the same start and end indices. If the search number does not appear in the dataset, return an empty list. If the dataset or search number is not provided, or if the dataset is not a list, return None. Assume that the dataset is sorted in ascending order.
"""

def binary_search(dataset, search_num, start=0, end=None):
    # Check for edge cases and handle them appropriately
    if dataset is None or search_num is None:
        return None
    if not hasattr(dataset, '__iter__'):
        return None
    if not dataset:
        return []
    if end is None:
        end = len(dataset) - 1
    if start > end: # If a number is not found
        return []
        
    mid = (start + end) // 2
    mid_val = dataset[mid]

    if mid_val < search_num: 
        return binary_search(dataset, search_num, mid + 1, end)
    elif mid_val > search_num: 
        return binary_search(dataset, search_num, start, mid - 1)
    else:
        start, end = mid, mid
        while start > 0 and dataset[start - 1] == search_num: 
            start -= 1
        while end < len(dataset) - 1 and dataset[end + 1] == search_num:
            end += 1
        return [start, end]