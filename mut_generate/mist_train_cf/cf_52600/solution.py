"""
QUESTION:
Write a function named `selection_sort` that takes a list of integers as input and returns the sorted list in increasing order using the selection sort method. The function should modify the input list in-place.
"""

def selection_sort(lst):
    # Traverse through all array elements
    for i in range(len(lst)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
                
        # Swap the found minimum element with the first element of 'unsorted' array        
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst