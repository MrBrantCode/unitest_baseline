"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of integers as input and returns the sorted list using the insertion sort algorithm with binary search. The function should determine the position of each element using binary search and then insert the element at that position. The input list is not guaranteed to be sorted initially, but the binary search will be applied to the sorted portion of the list during the sorting process.
"""

def insertion_sort(arr): 
    def binary_search(arr, val, start, end): 
        if start == end: 
            if arr[start] > val: 
                return start 
            else: 
                return start+1
  
        if start > end: 
            return start 
  
        mid = (start+end)//2
        if arr[mid] < val: 
            return binary_search(arr, val, mid+1, end) 
        elif arr[mid] > val: 
            return binary_search(arr, val, start, mid-1)
        else: 
            return mid 
  
    for i in range(1, len(arr)): 
        val = arr[i] 
        j = binary_search(arr, val, 0, i-1) 
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:] 
    return arr