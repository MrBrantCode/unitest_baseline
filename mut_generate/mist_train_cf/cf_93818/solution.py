"""
QUESTION:
Implement a function `count_unique_elements(arr)` that takes a list of integers as input, including possible negative numbers, and returns the count of unique elements in the list. The function must have a time complexity of O(n log n) and use constant space, i.e., not utilize any additional data structures such as sets or dictionaries.
"""

def count_unique_elements(arr):
    if len(arr) == 0:
        return 0
    
    arr.sort()
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    
    return count