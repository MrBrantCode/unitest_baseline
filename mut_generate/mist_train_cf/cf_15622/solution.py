"""
QUESTION:
Implement a count_unique_elements() function that takes a list of integers as input and returns the count of unique elements in the list. The function must have a time complexity of O(n) and use only constant space. The input list can contain negative numbers.
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