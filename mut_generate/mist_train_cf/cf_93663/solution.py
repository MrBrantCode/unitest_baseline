"""
QUESTION:
Design a function called `remove_duplicates` that takes an unsorted array of integers as input and returns the array with all duplicates removed and sorted. The function must have a time complexity of O(n) and handle negative numbers and zero. The function should also remove all occurrences of duplicates, not just one occurrence, and modify the original array in-place.
"""

def remove_duplicates(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    unique_arr = []
    for num in arr:
        if counts[num] == 1:
            unique_arr.append(num)
    
    arr[:] = sorted(unique_arr)
    return arr