"""
QUESTION:
Implement a function named `merge_sort` that sorts an array of elements in ascending order using a modified merge sort algorithm, which incorporates binary search to find the correct position for each element in the sorted subarray. The function should have a time complexity of O(nlogn) and a space complexity of O(n). The input is a list of elements, and the output is the sorted list. The function should be able to handle arrays with a length of 1 or more elements.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    
    for val in left:
        while i < len(right) and right[i] < val:
            merged.append(right[i])
            i += 1
        merged.append(val)
    
    merged.extend(right[i:])
    return merged