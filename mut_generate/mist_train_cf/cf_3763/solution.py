"""
QUESTION:
Implement the `merge_sort` function to sort an array of integers in descending order using the Merge Sort algorithm and keep track of the number of swaps made during the sorting process. If the array contains duplicate elements, sort them in descending order and then rearrange the duplicates in ascending order within their respective groups. The function should have a time complexity of O(n log n) and return both the sorted array and the number of swaps.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, swaps_left = merge_sort(arr[:mid])
    right, swaps_right = merge_sort(arr[mid:])
    
    sorted_arr, swaps_merge = merge(left, right)
    
    total_swaps = swaps_left + swaps_right + swaps_merge
    return sorted_arr, total_swaps

def merge(left, right):
    merged = []
    swaps = 0
    
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            swaps += len(left) - i
    
    merged += left[i:]
    merged += right[j:]
    
    return merged, swaps