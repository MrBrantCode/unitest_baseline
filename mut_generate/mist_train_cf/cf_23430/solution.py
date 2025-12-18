"""
QUESTION:
Implement a function named `binary_search` that performs a recursive binary search on a sorted list. The function should take in the list `arr`, the target number `num`, and the `start` and `end` indices as parameters. It should return the index of the target number if found, or `None` otherwise.
"""

def binary_search(arr, num, start, end):
    if start >= end: 
        return None

    mid = start + (end - start)//2
    if arr[mid] == num: 
        return mid 
  
    if arr[mid] < num: 
        return binary_search(arr, num, mid+1, end) 
    else: 
        return binary_search(arr, num, start, mid-1)