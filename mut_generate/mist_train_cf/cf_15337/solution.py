"""
QUESTION:
Design a function named `remove_duplicates` that takes an array of integers as input and returns the array with all duplicates removed in sorted order. The function should have a time complexity of O(n), where n is the number of elements in the array, and it should handle negative numbers and zero in the array.
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