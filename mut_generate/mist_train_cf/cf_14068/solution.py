"""
QUESTION:
Write a function `remove_duplicates_and_sort(arr)` that takes a list of integers as input, removes any duplicate numbers, sorts the remaining elements in descending order, and returns two lists: one containing the sorted unique elements and another containing the count of each unique element. The input list can contain duplicate integers, and the output lists should maintain the same order of elements.
"""

def remove_duplicates_and_sort(arr):
    # Remove duplicates
    unique_arr = list(set(arr))
    
    # Sort in descending order
    sorted_arr = sorted(unique_arr, reverse=True)
    
    # Count of each unique element
    count_arr = []
    for num in sorted_arr:
        count_arr.append(arr.count(num))
    
    return sorted_arr, count_arr